import { obtain } from "./prompts";
import { extractData,createFolder,type TarotCard } from "./readfile";
import { nameModel } from "./init";

await createFolder(nameModel);
let data:TarotCard[]|null=await extractData("./data/sample.json");
await obtain(data,true);
data=await extractData("./data/sample_es.json");
await obtain(data,false);
