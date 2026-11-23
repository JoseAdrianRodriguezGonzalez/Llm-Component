import pandas as pd 
df1=pd.read_csv("topics.csv")
df2=pd.read_csv("docs_with_topics.csv")
conteo=df2.groupby(["location","topic"]).size().reset_index(name="conteo")
conteo=conteo[conteo["topic"]!=-1]
conteo=conteo.sort_values(by=["location","conteo"],
                          ascending=[True,False])
top5=conteo.groupby("location").head(6)
df_final=top5.merge(
    df1[["Topic","Name"]],
    left_on="topic",
    right_on="Topic",
    how="left"
)
df_final.to_csv("Topicos_5.csv")
top5.to_csv("conteo.csv",index=False )
