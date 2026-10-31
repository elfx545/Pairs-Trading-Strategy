# Pairs Trading Research: Coca-Cola (KO) & PepsiCo (PEP)

Ce projet implémente une recherche quantitative sur une stratégie de **Pairs Trading** (trading par paires) appliquée à deux actifs censés être fortement corrélés : **Coca-Cola (KO)** et **PepsiCo (PEP)**.

##  Objectifs du Projet
* **Collecte et nettoyage de données financières** historiques avec l'API `yfinance`.
* **Analyse de cointégration et de corrélation** entre les deux actifs pour identifier une relation d'équilibre à long terme.
* **Visualisation des performances** et des écarts de prix (*spreads*) pour repérer des opportunités de retour à la moyenne (*mean reversion*).

---



```bash
pip install numpy pandas matplotlib yfinance