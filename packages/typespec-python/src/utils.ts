export function camelToSnakeCase(name: string): string {
    if (!name) return name;
    const camelToSnakeCaseRe = (str: string) =>
        str
            .replace(/[^a-zA-Z0-9]/g, "_")
            .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`)
            .replace(/_+/g, "_");

    return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

export function removeUnderscoresFromNamespace(name?: string): string {
    // needed because of the _specs_ tests
    return (name || "").replace(/_/g, "");
}
