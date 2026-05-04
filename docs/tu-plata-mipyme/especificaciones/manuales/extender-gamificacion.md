---
title: "Manual — Extender la gamificación"
description: "Receta paso a paso para agregar checklist items, tipos de milestone, tools nuevas, ajustar XP por etapa o cambiar niveles del árbol del emprendedor."
tags:
  - tu-plata-mipyme
  - manuales
  - gamificación
  - tool-calling
  - chat
---

# 📘 Extender el sistema de gamificación

!!! info ":material-information: Para qué sirve este manual"
    Receta paso a paso para extender el sistema de gamificación + tool calling sin tener que re-leer el código del repo. Cubre 6 escenarios comunes: agregar checklist items, milestones, tools, ajustar XP, cambiar niveles del árbol, y modificar visuales de píldoras.

## Componentes del sistema

```
apps/app/src/lib/
├── checklist/items.ts         # catálogo de checklist + XP por etapa + nivelFromXp
├── tools/definitions.ts       # JSON schemas que ve Claude
├── tools/executor.ts          # implementación server-side de cada tool
└── prompts/system.ts          # instrucciones al modelo (incluye lista de item_keys)

apps/app/src/components/chat/
└── ChatMessage.tsx            # KIND_STYLES (colores de los pills)

supabase/migrations/           # cambios estructurales de DB
```

**Spec relacionada (en el repo de código):** `docs/specs/fase-2-auto-update-perfil.md`

---

## 1. Agregar un checklist item nuevo

!!! example ":material-check-circle: Caso típico"
    Querés que el bot pueda marcar "ya tengo Transbank" como ítem hecho con XP asociado.

### Pasos

**1.1.** Editá `apps/app/src/lib/checklist/items.ts` y agregá la entrada:

```ts
'transbank-activado': {
  key: 'transbank-activado',
  etapa: 'E2',
  xp: 60,
  label: 'Transbank activado',
  description: 'Pasarela de pagos lista para vender con tarjetas.',
},
```

**1.2.** Editá `apps/app/src/lib/prompts/system.ts` y agregá el `item_key` a la lista del catálogo en la sección "Tools disponibles" (bullet de `mark_checklist_item`):

```
- `transbank-activado` (E2)
```

**1.3.** **No requiere migration.** Las entradas viven en código (TS), no en DB. La tabla `progress_checklist` ya soporta cualquier `item_key text`.

**1.4.** Build local + push:

```bash
pnpm --filter @impulsa/app build && git add -A && git commit -m "feat: agregar checklist item transbank-activado" && git push
```

### Verificar

- En el chat: *"acabo de activar Transbank"*
- El bot debería llamar `mark_checklist_item('transbank-activado')`
- Aparece píldora `✅ Transbank activado +60 XP`
- Header sube +60 XP

---

## 2. Agregar un tipo de milestone nuevo

!!! example ":material-check-circle: Caso típico"
    Querés celebrar "primer cliente recurrente" o "1.000 seguidores en Instagram".

### Pasos

**2.1.** Migration para agregar el tipo al CHECK constraint.

Crear `supabase/migrations/00NN_milestones_nuevos_tipos.sql`:

```sql
-- =============================================================================
-- 00NN_milestones_nuevos_tipos.sql
-- Fecha:       (al aplicar)
-- Autor:       <vos>
-- Descripción: Agrega tipos cliente_recurrente e instagram_1k a user_milestones.
-- Idempotente: sí.
-- =============================================================================

alter table public.user_milestones
  drop constraint if exists user_milestones_tipo_check;

alter table public.user_milestones
  add constraint user_milestones_tipo_check
  check (tipo in (
    'boleta',
    'sii_activo',
    'cuenta_empresa',
    'fondo_ganado',
    'primer_empleado',
    'marca_registrada',
    'cliente_recurrente',   -- nuevo
    'instagram_1k',         -- nuevo
    'otro'
  ));
```

**2.2.** Editá `apps/app/src/lib/tools/definitions.ts` (tool `record_milestone`, dentro del enum):

```ts
tipo: {
  type: 'string',
  enum: [
    'boleta', 'sii_activo', 'cuenta_empresa', 'fondo_ganado',
    'primer_empleado', 'marca_registrada',
    'cliente_recurrente',  // nuevo
    'instagram_1k',        // nuevo
    'otro',
  ],
},
```

**2.3.** Editá `apps/app/src/lib/tools/executor.ts` y agregá XP + emoji para los nuevos tipos:

```ts
const MILESTONE_XP: Record<string, number> = {
  // ... existentes
  cliente_recurrente: 30,
  instagram_1k: 50,
  otro: 20,
};

const MILESTONE_EMOJI: Record<string, string> = {
  // ... existentes
  cliente_recurrente: '🤝',
  instagram_1k: '📸',
  otro: '⭐',
};
```

**2.4.** Mencionar los tipos en el system prompt si querés que el bot los conozca explícitamente (ver `prompts/system.ts`, sección de `record_milestone`).

**2.5.** Aplicar migration en Supabase + actualizar `supabase/CHANGELOG.md` y `supabase/README.md`.

**2.6.** Build + push.

### Verificar

- *"hoy llegué a los 1.000 seguidores en Insta"*
- Bot llama `record_milestone(tipo='instagram_1k', descripcion='1.000 seguidores en Instagram')`
- Píldora `📸 1.000 seguidores +50 XP`

---

## 3. Agregar una tool nueva

!!! example ":material-check-circle: Caso típico"
    Querés que el bot pueda registrar un compromiso ("voy a hacer X la próxima semana") en una tabla de tareas.

### Pasos

**3.1.** Migration si la tool persiste en una tabla nueva:

```sql
create table if not exists public.user_compromisos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  texto text not null,
  fecha_objetivo date,
  cumplido boolean default false,
  created_at timestamptz not null default now()
);
-- + RLS análogo a user_milestones
```

**3.2.** Definición JSON schema en `apps/app/src/lib/tools/definitions.ts`:

```ts
{
  name: 'register_compromiso',
  description: 'Registra un compromiso que el usuario asume con una fecha. Ej: "voy a hacer mi inicio de actividades el lunes". Solo cuando el usuario lo dice explícito.',
  input_schema: {
    type: 'object',
    properties: {
      texto: { type: 'string' },
      fecha_objetivo: { type: 'string', description: 'YYYY-MM-DD' },
    },
    required: ['texto'],
  },
},
```

**3.3.** Implementación en `apps/app/src/lib/tools/executor.ts`:

```ts
async function registerCompromiso(input: unknown, ctx: ToolContext): Promise<ToolResult> {
  const i = input as { texto?: string; fecha_objetivo?: string };
  if (!i.texto) return { ok: false, message: 'texto requerido' };
  await ctx.supabase.from('user_compromisos').insert({
    user_id: ctx.userId,
    texto: i.texto,
    fecha_objetivo: i.fecha_objetivo ?? null,
  });
  return {
    ok: true,
    message: `Compromiso registrado: ${i.texto}`,
    ui: { kind: 'milestone', label: `Compromiso: ${i.texto}`, emoji: '📌' },
  };
}
```

**3.4.** Agregá el case al switch en `executeTool`:

```ts
case 'register_compromiso': return await registerCompromiso(input, ctx);
```

**3.5.** Documentar en system prompt cuándo usarla (regla "cuándo usar cada una") con ejemplo concreto + contraejemplo.

**3.6.** Si querés un nuevo color de píldora, agregá un `kind` nuevo a `ToolEventUi['kind']` en `ChatMessage.tsx` y al `KIND_STYLES`.

**3.7.** Build + push + aplicar migration.

!!! warning ":material-help-circle: Decisión clave: ¿da XP o no?"
    - **Sí (es un logro)** → usá `bumpXp(ctx.supabase, ctx.userId, N)` dentro de la tool.
    - **No (es solo registro)** → la tool no toca `profiles.xp`. Igual aparece píldora.

---

## 4. Ajustar XP por etapa

!!! example ":material-check-circle: Caso típico"
    Querés que subir a E3 dé 500 XP en vez de 300.

### Pasos

**4.1.** Editá `apps/app/src/lib/checklist/items.ts`:

```ts
export const XP_POR_ETAPA: Record<Etapa, number> = {
  E0: 0,
  E1: 50,
  E2: 150,
  E3: 500,   // antes 300
  E4: 800,   // ajusta también E4 si querés mantener escalado
};
```

**4.2.** **No requiere migration ni rollback de usuarios existentes.** El XP histórico de cada user en `profiles.xp` se queda como está; el cambio solo afecta a los próximos awarding.

**4.3.** Build + push.

!!! info ":material-information: Decisión D2 del spec"
    XP nunca se resta. Si querés "rebalancear" reseteando XP de los users actuales, eso es decisión de producto separada. Por defecto: avanzar y dejar.

---

## 5. Cambiar umbrales de niveles del árbol

!!! example ":material-check-circle: Caso típico"
    Querés que Brote sea 100-300 XP en vez de 200-500.

### Pasos

**5.1.** Editá `apps/app/src/lib/checklist/items.ts`, función `nivelFromXp`:

```ts
export function nivelFromXp(xp: number): Nivel {
  if (xp >= 800) return 'bosque';   // antes 1000
  if (xp >= 400) return 'arbol';    // antes 500
  if (xp >= 100) return 'brote';    // antes 200
  return 'semilla';
}
```

**5.2.** Recalcular nivel de usuarios existentes (one-shot SQL):

```sql
update public.profiles
set nivel = case
  when xp >= 800 then 'bosque'
  when xp >= 400 then 'arbol'
  when xp >= 100 then 'brote'
  else 'semilla'
end;
```

!!! warning ":material-alert: One-shot, no migration"
    Esto NO va como migration versionada (no es estructural, es rebalanceo de datos). Lo corrés una vez en el SQL Editor del dashboard.

**5.3.** El check constraint de `profiles.nivel` solo permite `('semilla','brote','arbol','bosque')`. Si agregás un nivel nuevo (ej: `gigante`), ahí sí necesitás migration:

```sql
alter table public.profiles drop constraint if exists profiles_nivel_check;
alter table public.profiles add constraint profiles_nivel_check
  check (nivel in ('semilla','brote','arbol','bosque','gigante'));
```

Y actualizar el type `Nivel` + `nivelFromXp` + cualquier UI que renderice el nivel.

**5.4.** Build + push.

---

## 6. Cambiar el color/emoji de un kind de píldora

!!! example ":material-check-circle: Caso típico"
    Querés que las píldoras de checklist sean amarillas en vez de verdes.

Editá `apps/app/src/components/chat/ChatMessage.tsx`:

```ts
const KIND_STYLES: Record<ToolEventUi['kind'], string> = {
  xp: 'border-purple bg-purple-light text-purple',
  checklist: 'border-yellow bg-amber-light text-amber',  // cambiado
  milestone: 'border-amber bg-amber-light text-amber',
  etapa: 'border-blue bg-blue-light text-blue-deep',
  negocio: 'border-border bg-fog text-mid',
};
```

Si necesitás un kind nuevo entero (ej: `'comunidad'` para algo de redes), agregalo al type union de `ToolEventUi['kind']` y al record. Después usalo en el ejecutor como `ui: { kind: 'comunidad', label: '...' }`.

---

## 7. Reglas de oro

!!! danger ":material-alert-octagon: Reglas que NO se relajan"

| # | Regla | Por qué |
|---|---|---|
| 1 | **Idempotencia siempre.** Si llamás 2 veces la misma tool con el mismo input, no debe doblar XP. | Evita que el bot abuse o que el usuario "hackée" repitiendo. |
| 2 | **Validá inputs en el ejecutor.** No confíes en que el modelo manda el shape correcto. | El JSON schema lo guía, no lo obliga. |
| 3 | **XP nunca se resta** (decisión D2 del spec). | UX: celebramos avances. Rollback no penaliza. |
| 4 | **Documentá cuándo NO usar la tool en el system prompt.** | Sin contraejemplos, el modelo abusa. |
| 5 | **`<tool-event>` se persiste serializado en `messages.content`.** | Las píldoras sobreviven a recargar página o cambiar de tab. |
| 6 | **Cada migration nueva → CHANGELOG + README de supabase actualizado.** | Trazabilidad para replicar la base el día del lab. |
| 7 | **Nunca edites una migration ya aplicada.** Crea una nueva que la corrija. | Preserva el historial de `supabase/migrations/` como source of truth. |

---

## 8. Checklist antes de pushear cambios al sistema de gamificación

- [ ] Build local pasa: `pnpm --filter @impulsa/app build`
- [ ] Si tocaste DB: migration creada en `supabase/migrations/` con header completo
- [ ] Si tocaste DB: `supabase/CHANGELOG.md` y `supabase/README.md` actualizados
- [ ] Si agregaste tool: regla del system prompt (cuándo usar / cuándo NO) + ejemplo
- [ ] Test manual: el bot llama la tool en el caso esperado
- [ ] Test manual: el bot NO la llama en el caso ambiguo
- [ ] Test manual: idempotencia — repetir el mismo trigger 2 veces no dobla efectos
- [ ] Commit con mensaje descriptivo (formato: `feat:` `fix:` `chore:`)
- [ ] Si la migration es destructiva o cambia constraints existentes: aviso al equipo antes de mergear

---

## 9. Próximas extensiones planeadas (out of scope hoy)

Cuando entren, aplicá la receta correspondiente:

| Extensión | Receta a usar |
|---|---|
| Tool de "consultar SII en vivo" via MCP | Sección 3 (tool nueva), pero el ejecutor llama API externa en vez de Supabase |
| Tool de "generar carta al banco" | Sección 3, devuelve documento generado en `result.message` con link |
| Tipo milestone "exporto al extranjero" | Sección 2 |
| Nivel "gigante" >5000 XP para PYMES grandes | Sección 5 + migration de constraint |
| Ajuste de XP global por feedback de usuarios | Secciones 4 y 5 |

---

## Referencias

- **Spec original (en repo de código):** [`docs/specs/fase-2-auto-update-perfil.md`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/docs/specs/fase-2-auto-update-perfil.md){target="_blank"}
- **Repo de código:** [`impactlab_pre_journeyemprendedor`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor){target="_blank"}
- **Plan de implementación:** [plan.md](../../plan.md)
- **PRD:** [PRD.md](../../PRD.md)
