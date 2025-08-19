import { obtain } from "./prompts";
import { extractData,createFolder,type TarotCard } from "./readfile";
import { availableModels,loadAvailableModels} from "./init";
loadAvailableModels();
for (const models of availableModels) {
   // await createFolder(models);
    let data:TarotCard[]|null=await extractData("./data/sample.json");
    //await obtain(data,true,models);
    data=await extractData("./data/sample_es.json");
    await obtain(data,false,models);
    
}
