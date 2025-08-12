import {fileURLToPath} from "url";
import path from "path";
import chalk from "chalk";
import {getLlama, LlamaChatSession, LlamaModel, resolveModelFile} from "node-llama-cpp";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const modelsDirectory = path.join(__dirname, "..", "models");
let model:LlamaModel;
export const nameModel="astramix_l2_7b_Q5_K_M"
export const initializeModel =async()=>{

    const llama = await getLlama({gpu:'cuda'});
    console.log(llama.systemInfo)
    console.log(chalk.bgRed('Loading the file....'))
    const modelPath = await resolveModelFile(
        nameModel+".gguf",
        modelsDirectory
    );
    
    console.log(chalk.yellow('Loading the model...'));
    model= await llama.loadModel({modelPath});
    return model;
}   
export const createSession =async ()=>{
    console.log(chalk.green('creating context...'));
    const context=await model.createContext();
    console.log(chalk.green('Model instanced correctly'));
    return new LlamaChatSession({
        contextSequence: context.getSequence()
    });
}