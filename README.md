# minite

**minite** is a lightweight, open-source toolchain for working with Minecraft mods across versions.

Its first component, the resolver, focuses on answering one brutally practical question:

> “What is the newest Minecraft Java Edition version where *all* of these mods actually exist?”

No guesswork. No launchers. No magic.

---

## minite-resolver (v0)

`minite-resolver` is the core logic module of minite.

### What it does
- Accepts a list of Minecraft mod names
- Queries Modrinth for **Fabric-compatible** releases
- Computes the **intersection of supported Minecraft versions**
- Outputs the **highest compatible version**, or a clear failure reason

### What it does NOT do
- Download mods
- Resolve mod dependencies
- Support Forge or Quilt
- Act as a launcher or modpack manager
- Provide a GUI (yet)

This is a resolver, not a platform.

---

## Scope Philosophy

minite is intentionally narrow in scope.

Each component should:
- Do one thing
- Be explicit
- Fail clearly

Complexity is added only when it earns its place.

---

## Data Source
- Modrinth API only

## Loader Support
- Fabric only (v0)

---

## Status
Early prototype.  
Interfaces may change.  
Core logic is intentionally simple and inspectable.

---

## Planned (Out of Scope for v0)
- Web interface
- Better mod name disambiguation
- Optional dependency inspection
- Bulk download orchestration

These are future layers, not current goals.

---

## Legal
minite is an independent, open-source project and is **not affiliated with or endorsed by Ninite**.

---

## License
Apache License 2.0