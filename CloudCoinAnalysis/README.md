# CloudCoinAnalysis


Analysis of the 3 main cryptocurrencies offering a cloud computing solution:  GOLEM, SONM, IEXEC and Bitcoin.    

The application runs on top of iExec platform and generate a market report, it performs exploratory data analysis
and use machine learning algorithm to predict market prices in future 30 days for the above 3 cryptocurrencies and Bitcoin.


## About iExec:

iExec is building the future of the Internet infrastructure by decentralizing the cloud computing market. It is the first blockchain-based cloud computing marketplace.
The iExec network connects cloud resource sellers with cloud resource buyers, encouraging an ecosystem of decentralized and autonomous, privacy-preserving applications.
This network aims at providing companies with scalable, secure and easy access to the services, datasets and computing resources they need. iExec’s technology relies on Ethereum smart contracts and allows for a virtual cloud infrastructure that provides high-performance computing services on-demand.


## Data and algorithm source:

The code is forked from:

* https://github.com/jieyima/Cryptocurrency_Investment_Analysis_and_Modeling for the analysis part

* https://github.com/JesseVent/crypto to build datasets


## Create and store datasets on your data wallet

The Crypto R package helps to download historical Cryptocurrency Prices For any Tokens using the CoinMarketCap API

### Generate the dataset file

The getcloudcoin.R script generates the csv dataset file, containing the full history for BTC, GNT, SNM and RLC cryptos.

```
 Rscript getcloudcoin.R
```

Then create the zip file and place the zip in the dataset repo.
```
zip dataset/cloudcoin_2019-05-06.zip cloudcoin_2019-05-06.csv
 adding: cloudcoin_2019-05-06.csv (deflated 67%)
```

## Installing iExec

Follow instructions to install the SDK and set up your wallet  
https://docs.iex.ec/gettingstarted.html
and
https://docs.iex.ec/wallet.html

In this demo, 2 wallet has been generated for both developer and data owner: **developer_wallet** and **data_owner_wallet**.      
The sdk options **--wallet_file=** will be used to select the good owner for all commands.  

### Register the dataset on the blockchain

Let's register the dataset, the dataset is not store on the blockchain ethereum, the blockchain is only use to manage the ownership, the access and the monetization.

```
iexec dataset init --wallet-file data_owner_wallet
```
Edit the dataset info in iexec.json file.

The dataset file must have a public access.  

The checksum will be use to check the integrity on the file (not implemented).

```
"dataset": {
  "owner": "0x9CdDC59c3782828724f55DD4AB4920d98aA88418",
  "name": "cloincoin-dataset-20190506",
  "multiaddr": "https://raw.githubusercontent.com/iExecBlockchainComputing/apps/master/CloudCoinAnalysis/dataset/cloudcoin_2019-05-06.zip",
  "checksum": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
Deploy

```
iexec dataset deploy --wallet-file data_owner_wallet
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
✔ Deployed new dataset at address 0x62E2750208114e9ABAB091D077553623a54B0d57

```

### Publish selling order for the dataset.

As the dataset is now registered and the ownership is stored on the blockchain; the owner has to publish order defining the price, the volume and restrictions for the usage of the dataset.

```
iexec order init --dataset --wallet-file data_owner_wallet
ℹ using chain [kovan]
✔ Saved default datasetorder in "iexec.json", you can edit it:
dataset:            0x62E2750208114e9ABAB091D077553623a54B0d57
datasetprice:       0
volume:             1000000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
apprestrict:        0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000

```

Let's create an order with 10 nRLC cost and a volume of 1000 tasks with no extra restriction, regarding the application or a workerpool or any end-users.
The dataset created should be extensively used.   

Edit the iexec.json file.

```
"datasetorder": {
  "dataset": "0x62E2750208114e9ABAB091D077553623a54B0d57",
  "datasetprice": 10,
  "volume": 1000,
  "tag": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "apprestrict": "0x0000000000000000000000000000000000000000",
  "workerpoolrestrict": "0x0000000000000000000000000000000000000000",
  "requesterrestrict": "0x0000000000000000000000000000000000000000"
}
```

Sign the order

```
iexec order sign --dataset --wallet-file data_owner_wallet
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
✔ datasetorder signed and saved in orders.json, you can share it:
dataset:            0x62E2750208114e9ABAB091D077553623a54B0d57
datasetprice:       10
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
apprestrict:        0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xaecbab832d62f27b8980a8ad16ab3ad1e8c2556e0501c129ce6a7d5d357acca7
sign:               0x3a8556cfa18d7639a5069b65316b4e209a26e8a36c3c3eac50e46fdbf5fb46da4d2054d4e6e1065258918c8fe2aadbeddd8a74380c60d8caf7de868a5786d0091b
```
and then publish the order

```
iexec order publish --dataset --wallet-file data_owner_wallet
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
? Do you want to publish the following datasetorder?
dataset:            0x62E2750208114e9ABAB091D077553623a54B0d57
datasetprice:       10
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
apprestrict:        0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xaecbab832d62f27b8980a8ad16ab3ad1e8c2556e0501c129ce6a7d5d357acca7
sign:               0x3a8556cfa18d7639a5069b65316b4e209a26e8a36c3c3eac50e46fdbf5fb46da4d2054d4e6e1065258
918c8fe2aadbeddd8a74380c60d8caf7de868a5786d0091b
 Yes
✔ datasetorder successfully published with orderHash 0x330d22f55924fa0bf7573ebfcc67b37123c89dbb6b4dd4f8a68eaeca9dad76f6
```

Check the order status

```
iexec order show --dataset 0x1ad297bfb4aa01d04c8c8919f224b304b043bbe7e5c56616a8a27f7f668595dd
ℹ using chain [kovan]
✔ datasetorder with orderHash 0x1ad297bfb4aa01d04c8c8919f224b304b043bbe7e5c56616a8a27f7f668595dd details:
orderHash:            0x1ad297bfb4aa01d04c8c8919f224b304b043bbe7e5c56616a8a27f7f668595dd
order:
  dataset:            0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E
  datasetprice:       10
  volume:             1000
  tag:                0x0000000000000000000000000000000000000000000000000000000000000000
  apprestrict:        0x0000000000000000000000000000000000000000
  workerpoolrestrict: 0x0000000000000000000000000000000000000000
  requesterrestrict:  0x0000000000000000000000000000000000000000
  salt:               0x5f70873d19c66377c8b03c57fa108c94153e9fc20549216b8b74fed2ee030082
  sign:               0x343c2b251e5ec169c94b989e01620aaddfaa2fe8dc7676e915c55b3ebe1454fa5b6dcbf9c4e9aacdd612725a108b6677cd7976cffe76a8c50a3a19c90847c2281b
remaining:            1000
status:               open
publicationTimestamp: 2019-05-03T12:02:54.960Z
signer:               0x9CdDC59c3782828724f55DD4AB4920d98aA88418
```

## Deploy the application

The application can process all datasets created as above

The application is available at
https://cloud.docker.com/u/iexechub/repository/docker/iexechub/cloudcoin/general

Source code in the current repository.

### Register applications on the blockchain

The registration is similar to the dataset registration.
First, we will register the application and then publish orders with defining price, volume and restriction.

```
iexec app init
```

Edit iexec.json file, and set up the name, the address and the hash of the docker image
For a docker the checksum is obtained with a docker of the image
Do not forget to add a "0x" prefix to the hash.

```
"app": {
    "owner": "0x47d0Ab8d36836F54FD9587e65125Bbab04958310",
    "name": "CloudCoin",
    "type": "DOCKER",
    "multiaddr": "registry.hub.docker.com/iexechub/cloudcoin",
    "checksum": "0x5496bd85e2b787b3a84dc7fb53e4d2c952f9eab13419e0f496be7eeefcc66bd6",
    "mrenclave": ""
  },
```

Deploy the application

```
iexec app deploy --wallet-file developer_wallet
ℹ using chain [kovan]
? Using wallet developer_wallet
Please enter your password to unlock your wallet [hidden]
✔ Deployed new app at address 0xe8dab3a22C6B5077796437a980C6F303f9763239
```

### Publish app order

Create the  configuration section in iexec.json

```
iexec order init --app
ℹ using chain [kovan]
✔ Saved default apporder in "iexec.json", you can edit it:
app:                0x814FCFf7aa640F3b59CADF8011F89B55D3De3368
appprice:           0
volume:             1000000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
datasetrestrict:    0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000

```

Set up price, volume and restriction
For this app, restriction are not required.
Sign and publish app order

Price : 1 nRLC
Volume : 1000

```
iexec order sign --app --wallet-file developer_wallet
ℹ using chain [kovan]
? Using wallet developer_wallet
Please enter your password to unlock your wallet [hidden]
✔ apporder signed and saved in orders.json, you can share it:
app:                0xe8dab3a22C6B5077796437a980C6F303f9763239
appprice:           1
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
datasetrestrict:    0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xbf0d689dd08cac63f33c110d3d183e6d3ad49841c268589da3e1a5b7c639033b
sign:               0x22a7307c7704d98d9fcac4af0d93628ae9c1e420b2cbeababb0674592c94626963f5fa8e29ed6a5e9d7c8ac707dd5ebc6fbee8e93df1f6a78930f8865977e9c91b


```

```
iexec order publish --app --wallet-file developer_wallet
ℹ using chain [kovan]
? Using wallet developer_wallet
Please enter your password to unlock your wallet [hidden]
? Do you want to publish the following apporder?
app:                0xe8dab3a22C6B5077796437a980C6F303f9763239
appprice:           1
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
datasetrestrict:    0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xbf0d689dd08cac63f33c110d3d183e6d3ad49841c268589da3e1a5b7c639033b
sign:               0x22a7307c7704d98d9fcac4af0d93628ae9c1e420b2cbeababb0674592c94626963f5fa8e29ed6a5e9d
7c8ac707dd5ebc6fbee8e93df1f6a78930f8865977e9c91b
Yes
✔ apporder successfully published with orderHash 0xc869749b88c7f6a58c64aa847c1c8cf723191dd3aa7b335a5f7a16b3d0f3a218
```
### Test locally the app with dataset
```
rm -rf iexec_in iexec_out
mkdir iexec_in iexec_out
cp dataset/cloudcoin_2019-05-06.zip iexec_in/. docker run -v `pwd`/iexec_in:/iexec_in -v `pwd`/iexec_out:/iexec_out -e DATASET_FILENAME="cloudcoin_2019-05-06.zip" iexechub/cloudcoin
```

## Buy a crypto coin analysis and get your daily report

Your report contains a market report with a collection of plots    

![Candle stick](images/cancdlestick_chart_for_rlc.png)
![RoI](images/roi.png)

### Method 1: from the marketplace

https://v3.market.iex.ec.

This is possible to process a cloud coin analysis   
You only need the dataset and dapp addresses deployed just created, the markeplace is able to find the corresponding orders.
The corresponding addresses were given by **iexec app deploy** and **iexec dataset deploy** command

![buy a analysis](images/buy.png)

### Method 2 : using requestorder

TBD

## Get updated data

Information from CoinMarketCap is daily updated, so new dataset can be created everyday without changing the existing application, the app has no dataset restriction and is self-adaptable to date changes.
Similarly, it is recommended to improve the application and add new feature for a better analysis.


## Future work/next step:

 * Best prediction algorithm.
 * Use iExec security layers for data privacy.
