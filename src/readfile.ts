import * as fs from "fs/promises";

interface TarotCard {
    card: string;
    element: string;
    description: string;
}

const rawData = await fs.readFile("./data/sample_es.json", "utf-8");
export const data: TarotCard[] = JSON.parse(rawData);

export const createFolder = async (name: string): Promise<void> => {
    try {
        await fs.mkdir(`./output/${name}`, { recursive: true });
        console.log("Directory created successfully");
    } catch (err) {
        console.error("Error creating directory:", err);
    }
};

export const saveResponses = async (filePath: string, data: string): Promise<void> => {
    try {
        await fs.writeFile(filePath, data, "utf-8");
        console.log(`Archivo guardado correctamente en ${filePath}`);
    } catch (error) {
        console.log("No se pudo guardar", error);
    }
};
