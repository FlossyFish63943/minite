# Minite

**Minite** is a lightweight, open-source toolchain for reasoning about Minecraft mod compatibility across versions.

Its first component, the resolver, answers one brutally practical question:

> “What is the newest Minecraft Java Edition version where *all* of these mods actually exist?”

No guesswork.  
No launchers.  
No magic.

---

## minite-resolver (v0.1)

`minite-resolver` is the core logic module of Minite.

### What it does
- Accepts a list of Minecraft mod names
- Queries Modrinth for **Fabric-compatible** releases
- Computes the **intersection of supported Minecraft versions**
- Outputs:
  - A **sorted list** of compatible versions
  - The **highest compatible Minecraft version**, clearly highlighted
- Fails explicitly on:
  - Zero mods
  - Typo’d or missing mod names
  - No shared compatible versions

### What it does NOT do
- Download mods
- Resolve mod dependencies
- Support Forge or Quilt
- Act as a launcher or modpack manager
- Provide a GUI

This is a resolver, not a platform.

---

## Scope Philosophy

Minite is intentionally narrow in scope.

Each component should:
- Do one thing
- Be explicit
- Be inspectable
- Fail clearly

Complexity is added only when it earns its place.

---

## Data Source
- Modrinth API only

## Loader Support
- Fabric only (v0.1)

---

## Status
**v0.1 — Initial functional release**

- Core resolver logic implemented
- Deterministic version sorting
- Edge cases handled
- Interfaces still subject to change

---

## Planned (Out of Scope for v0.1)
- Forge / Quilt support
- Dependency resolution
- Web or GUI frontend
- Smarter mod name disambiguation
- Mod download orchestration

These are future layers, not current goals.

---

## Legal
Minite is an independent, open-source project and is **not affiliated with or endorsed by Ninite**.

---

## License
Apache License 2.0