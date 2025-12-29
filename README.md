# minite-resolver

minite-resolver is a small, focused tool that determines the **highest Minecraft Java Edition version**
for which **all given mods have Fabric-compatible releases**.

It is designed to answer one question clearly and honestly:

> “What is the newest Minecraft version where all these mods actually exist?”

## Scope (v0)

**What it does**
- Accepts a list of Minecraft mod names
- Queries Modrinth for Fabric-compatible releases
- Computes the intersection of supported Minecraft versions
- Outputs the highest compatible version, or a clear failure reason

**What it does NOT do**
- Download mods
- Resolve mod dependencies
- Support Forge or Quilt
- Provide a GUI (yet)
- Act as a launcher or modpack manager

This is a resolver, not a platform.

## Data Source
- Modrinth API only

## Loader
- Fabric only

## Status
Early prototype.  
Interfaces may change.  
Core logic is intentionally simple and explicit.

## Planned Extensions (out of scope for v0)
- Web interface
- Better mod name disambiguation
- Optional dependency inspection

These are future considerations, not current goals.

## License
Apache License 2.0
