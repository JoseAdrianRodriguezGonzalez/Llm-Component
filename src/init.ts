import {fileURLToPath} from "url";
import path from "path";
import chalk from "chalk";
import fs from "fs";
import {getLlama, LlamaChatSession, LlamaModel, resolveModelFile} from "node-llama-cpp";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const modelsDirectory = path.join(__dirname, "..", "models");
let model:LlamaModel;
//export const nameModel="aya-23-8B-Q6_K"
export let availableModels: string[] = [];
export const loadAvailableModels = () => {
    availableModels = fs.readdirSync(modelsDirectory)
        .filter(file => file.toLowerCase().endsWith(".gguf"))
        .map(file => file.replace(/\.gguf$/i, ""));
    
    if (availableModels.length === 0) {
        console.error(chalk.red("No se encontraron modelos .gguf en la carpeta de modelos"));
        process.exit(1);
    }
    console.log(chalk.blue("Modelos disponibles:"), availableModels);
};
export const initializeModel =async(nameModel:string)=>{

    const llama = await getLlama({gpu:'metal'});
    console.log(llama.systemInfo)
    console.log(chalk.bgRed('Loading the file....'))
    const modelPath = await resolveModelFile(
        nameModel+".gguf",
        modelsDirectory
    );
    
    console.log(chalk.yellow('Loading the model...'));
    model= await llama.loadModel({
        modelPath,
        gpuLayers:9999,
        contextSize:16384,
        batchSize:512,
        useMmap:true,useMlcache:true,
    });
    return model;
}   
export const createSession =async (language:boolean)=>{
    console.log(chalk.green('creating context...'));
    const context=await model.createContext();
    console.log(chalk.green('Model instanced correctly'));
    return new LlamaChatSession({
        systemPrompt: language?"":"Responde siempre en español de manera clara y natural.",
        contextSequence: context.getSequence(),
        conversationHistoryMaxMessages: 50,
        conversationHistoryMaxTokens: 1000,
        
    });
}
export const freeModel = () => {
    if (model) {
        console.log(chalk.red("Liberando modelo de memoria..."));
        model.dispose();
    }
};