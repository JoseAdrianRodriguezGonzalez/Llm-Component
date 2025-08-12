import chalk from "chalk";
import * as fs from "fs/promises";

export interface TarotCard {
    card: string;
    element: string;
    description: string;
}

export const extractData = async(path:string): Promise<TarotCard[]|null>=>{
    let data: TarotCard[]|null=null;
    try{
        const rawData = await fs.readFile(path, "utf-8");
        data = JSON.parse(rawData);
        console.log(chalk.green("Datos extraídos correctamente"))
    }catch(err){
        console.log("No se encontro dirección \n",err);
    }
    return data;
}
export const createFolder = async (name: string): Promise<void> => {
    const basePath:string=`./output/${name}`;
    try {
        await fs.mkdir(basePath, { recursive: true });
        await fs.mkdir(`${basePath}/en`, { recursive: true });
        await fs.mkdir(`${basePath}/es`, { recursive: true });
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
