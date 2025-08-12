import chalk from "chalk";
import { createSession,initializeModel,nameModel } from "./prompts";
import { data,createFolder,saveResponses} from "./readfile";
await initializeModel();
const session =await createSession();
await createFolder(nameModel);
let id:number=0;
for(const cards of data){
    const prompt=
    `Eres un lector de tarot. Dada una carta del tarot y un tema contextual, responde con una lectura simbólica y poética.  
    No menciones la carta ni el contexto explícitamente.  
    No expliques tu razonamiento ni desgloses los significados.  
    Evita dar consejos de vida.  
    Tu lectura debe ser abstracta y dejar espacio para la interpretación.  
    Responde con un solo párrafo de menos de 200 palabras.  
    Sin títulos, sin listas, sin formato.  
    Carta: ${cards.card}  
    Contexto: ${cards.element}. ${cards.description}  
    Ahora responde solo con la lectura.
    `;
    const response=await session.prompt(prompt);
    await saveResponses(`./output/${nameModel}/${id}.txt`,response);
    console.log(chalk.green(`Respuesta guardada para carta #${id}: ${cards.card}`));
    id++;
}
