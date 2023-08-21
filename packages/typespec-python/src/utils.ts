export function camelToSnakeCase(name: string): string {
    if (!name) return name;
    const camelToSnakeCaseRe = (str: string) =>
        str
            .replace("/", "_")
            .replace(/\s+/g, "_")
            .replace(/\$/g, "")
            .replace(/-/g, "_")
            .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

    return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}
