import { fileURLToPath } from "url";
import path from "path";
import { getLlama,LlamaChatSession } from "node-llama-cpp";
import chalk from "chalk";

const __dirname=path.dirname(fileURLToPath(import.meta.url));
const llama=await getLlama();
const model=await llama.loadModel({
    modelPath:path.join(__dirname,"..","models","hf_mradermacher_DeepSeek-R1-Distill-Llama-8B.Q8_0.gguf")
});
const context=await model.createContext();
const session=new LlamaChatSession({
    contextSequence:context.getSequence()
});
const q1="Hi there, how are you?";
console.log(chalk.bgYellow("User")+q1);
const a1= await session.prompt(q1);
console.log(chalk.blue("AI")+a1);

const q2 = "What is a genetic algorithm?";
console.log(chalk.yellow("User: ") + q2);

const a2 = await session.prompt(q2);
console.log(chalk.blue("AI: ") + a2);