import seaborn as sns

class TabelaTurmas:
    def __init__(self,dataframe) -> None:
        self.df = dataframe

    def distribuicao_periodo(self):
        sns.displot(data=self.df,x='Periodo')
    
    def getNomes(self):
        return list(self.df['Nome'])