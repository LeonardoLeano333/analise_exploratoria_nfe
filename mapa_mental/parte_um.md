TODO:
- tipo do dado: dados de compras (orders), pessoas (people) e devoluções (returns).()
- analise exporatoria dos dados buscando anomalias
    - sugerir melhorias
    - analises
    - alertas
    - monitoramentos
    - soluções com suas vantagens e desvantagens
    - fazer visualizações
    - levantar hipoteses
        - churn?
        - devolucoes, porque ocorrem?
        - classificacao de perfil de pessoa(clusterizacao?)? 
        - precos?
        Estatisticas sobre a eficiencia dos metodos matrix de confusão etc
- apontar KPIs (key performance indicator)


## Analises possiveis

- colunas relevantes:
    - location: city, state, region
    - category do produto: category, subcategory
    - mapa de segmento do cliente: segment
    - sales: sales(value), quantity, profit
    - shipping: tempo de trafego, tipo de envio

perguntas relevantes:
    - profit negativo (alerta) (AP)
    - maior profit (insight) (AG)
    - menor profit (alerta) (AP/AG)
    - soma geral do profit (report insight) (AG)
    - soma do profit por regiao (insight/alerta) (AG/AP)
    - soma do profit por segment (insight/alerta) (AG/AP)
    - media dos profit positivos (AG)
    - media dos profit negativos (AP)
    - media do profit por regiao (insight/alerta) (AG/AP)
    - media do profit por segment (insight/alerta) (AG/AP)
    - tempo de trafego do produto (ship date) - (Order Date) (CS)
    - tempo de trafego medio por regiao (insight/alerta) (CS)
    - relacionamento dos pedidos dos retornos analise do porque existe retorno (melhoria na experiencia do cliente final)

categorizar as analizes:
- (AP) analise de perdas
- (AG) analise de ganhos possiveis
- (CS) melhoria na experiencia do cliente final
