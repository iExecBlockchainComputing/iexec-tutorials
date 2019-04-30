# CloudCoinAnalysis


Analysis of the 3 main cryptocurrencies for the cloud computing supported by golem, sonm and iexec   


The application runs on top of iExec platform and generate a report, it performs exploratory data analysis
and builds machine learning models to predict market prices in future 30 days for the above 3 cryptocurrencies.

About iExec
iExec is building the future of the Internet infrastructure by decentralizing the cloud computing market. It is the first blockchain-based cloud computing marketplace.
The iExec network connects cloud resource sellers with cloud resource buyers, encouraging an ecosystem of decentralized and autonomous, privacy-preserving applications.
This network aims at providing companies with scalable, secure and easy access to the services, datasets and computing resources they need. iExec’s technology relies on Ethereum smart contracts and allows for a virtual cloud infrastructure that provides high-performance computing services on-demand.


Source:
The code is derivated from:
* https://github.com/jieyima/Cryptocurrency_Investment_Analysis_and_Modeling for the analysis part
* https://github.com/JesseVent/crypto for the building dataset


An application to analyse cryto tokens using datasets corresponding to the more.

Building datasets:

The Crypto R package helps to download historical Cryptocurrency Prices For all Tokens,
using the CoinMarketCap API

The following download the full history for BTC, GNT, SNM and RLC cryptos.

Rscript getcloudcoin.R

It generates a dataset you can propose to the market.


Future work:
