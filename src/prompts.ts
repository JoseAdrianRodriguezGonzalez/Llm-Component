import chalk from "chalk";
import { createSession,freeModel,initializeModel } from "./init";
import { saveResponses, type TarotCard} from "./readfile";
import { table } from "console";
function buildPrompt(card: TarotCard, language: boolean): string {
    if (language) {
        return `You are a tarot reader. Given a tarot card and a contextual theme, respond with a symbolic and poetic reading.
                Do not mention the card or context explicitly.
                Do not explain your reasoning or break down meanings.
                Avoid giving life advice.
                Your reading should be abstract and leave room for interpretation.
                Respond with a single paragraph under 200 words.
                No titles, no lists, no formatting.
                Card: ${card.card}
                Context: ${card.element}. ${card.description}
                Now respond with the reading only.`;
    } else {
        return `Eres un lector de tarot. Dada una carta del tarot y un tema contextual, responde con una lectura simbólica y poética.
                No menciones la carta ni el contexto explícitamente.
                No expliques tu razonamiento ni desgloses los significados.
                Evita dar consejos de vida.
                Tu lectura debe ser abstracta y dejar espacio para la interpretación.
                Responde con un solo párrafo de menos de 200 palabras.
                Sin títulos, sin listas, sin formato.
                Carta: ${card.card}
                Contexto: ${card.element}. ${card.description}
                Ahora responde solo con la lectura.`;
    }
}
export const obtain= async(dataRow:TarotCard[]|null,language:boolean,nameModel:string):Promise<void>=>{
    if(!dataRow){
        console.log(chalk.red("Dato nullo"))
        return;
    }
    await initializeModel(nameModel);
    const session =await createSession(language);
    
    try{

        for(let id=0;id<dataRow.length;id++){
            const card:TarotCard = dataRow[id]!;
            const prompt=buildPrompt(card,language);
            session.resetChatHistory();
            const response=await session.prompt(prompt);
            const filePath = `./output/${nameModel}/${language ? "en" : "es"}/${id}.txt`;
            await saveResponses(filePath,response);
            console.log(chalk.green(`Respuesta guardada para carta #${id}: ${card.card}`));
        }
    }
    finally{
        
        session.dispose();
        freeModel()
    }
}
