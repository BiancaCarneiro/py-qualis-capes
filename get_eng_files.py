from src.qualis_capes import QualisCapes
import pandas as pd

qualis = QualisCapes()

def update_qualis():
    print(qualis.last_update)
    qualis.update_data()


def main():
    update_qualis()
    
    # df = qualis.by_area("engenharias")
    
    # estratos = ["A2", "A3", "A4"]
    # df_filter = df.loc[df["Estrato"] == "A1"]
    # for est in estratos:
    #     df_filter = pd.concat((df_filter, df.loc[df["Estrato"] == est]))
    
    
    # df_filter.to_csv("dados_filtrados.csv", index=False)
    
if __name__ == "__main__":
    main()