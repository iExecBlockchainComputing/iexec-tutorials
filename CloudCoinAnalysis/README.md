# CloudCoinAnalysis


Analysis of the 3 main cryptocurrencies offering a cloud computing solution:  GOLEM, SONM and IEXEC   


The application runs on top of iExec platform and generate a market report, it performs exploratory data analysis
and use machine learning algorithm to predict market prices in future 30 days for the above 3 cryptocurrencies and Bitcoin.


## About iExec:

iExec is building the future of the Internet infrastructure by decentralizing the cloud computing market. It is the first blockchain-based cloud computing marketplace.
The iExec network connects cloud resource sellers with cloud resource buyers, encouraging an ecosystem of decentralized and autonomous, privacy-preserving applications.
This network aims at providing companies with scalable, secure and easy access to the services, datasets and computing resources they need. iExec’s technology relies on Ethereum smart contracts and allows for a virtual cloud infrastructure that provides high-performance computing services on-demand.


Source:
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
 zip dataset/cloudcoin_2019-05-02.zip cloudcoin_2019-05-02.csv
```

### Register the dataset on the blockchain

Let's register the dataset, the dataset is not store on the blockchain ethereum, the blockchain is only use to manage the ownership, the access and the monetization.

```
iexec dataset init  
```
Edit the dataset info in iexec.json file.

The dataset file must have a public access.  

The checksum will be use to check the integrity on the file (not implemented).

```
"dataset": {
  "owner": "0x9CdDC59c3782828724f55DD4AB4920d98aA88418",
  "name": "cloincoin-20190502-dataset",
  "multiaddr": "https://raw.githubusercontent.com/iExecBlockchainComputing/apps/master/CloudCoinAnalysis/dataset/cloudcoin_2019-05-02.zip",
  "checksum": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
Deploy

```
iexec dataset deploy
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
✔ Deployed new dataset at address 0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E
```

### Publish selling order for the dataset.

As the dataset is now registered and ownership is stored on the blockchain; the owner has to publish order defining the price, the volume and restrictions for the usage of the dataset.

```
iexec order init --dataset
```

Let's create an order with 10 nRLC cost and 1000 tasks allowed with no extra restriction.
This dataset has no restricted usage for user, worker pool and app.

Edit the iexec.json file.

```
    "datasetorder": {
      "dataset": "0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E",
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
iexec order sign --dataset
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
✔ datasetorder signed and saved in orders.json, you can share it:
dataset:            0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E
datasetprice:       10
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
apprestrict:        0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0x5f70873d19c66377c8b03c57fa108c94153e9fc20549216b8b74fed2ee030082
sign:               0x343c2b251e5ec169c94b989e01620aaddfaa2fe8dc7676e915c55b3ebe1454fa5b6dcbf9c4e9aacdd612725a108b6677cd7976cffe76a8c50a3a19c90847c2281b

```
and then publish the order

```
iexec order publish --dataset
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
? Do you want to publish the following datasetorder?
dataset:            0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E
datasetprice:       10
volume:             1000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
apprestrict:        0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0x5f70873d19c66377c8b03c57fa108c94153e9fc20549216b8b74fed2ee030082
sign:               0x343c2b251e5ec169c94b989e01620aaddfaa2fe8dc7676e915c55b3ebe1454fa5b6dcbf9c4e9aacdd6
12725a108b6677cd7976cffe76a8c50a3a19c90847c2281b
 Yes
✔ datasetorder successfully published with orderHash 0x1ad297bfb4aa01d04c8c8919f224b304b043bbe7e5c56616a8a27f7f668595dd
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
iexec app int
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
iexec app deploy
ℹ using chain [kovan]
? Using wallet developper_wallet
Please enter your password to unlock your wallet [hidden]
✔ Deployed new app at address 0x814FCFf7aa640F3b59CADF8011F89B55D3De3368
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

```
iexec order sign --app
ℹ using chain [kovan]
? Using wallet developper_wallet
Please enter your password to unlock your wallet [hidden]
✔ apporder signed and saved in orders.json, you can share it:
app:                0x814FCFf7aa640F3b59CADF8011F89B55D3De3368
appprice:           0
volume:             1000000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
datasetrestrict:    0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xe0fe46a67f63ce09a5e0e847f6615111733b25db3dfd3086b216f6410201a14e
sign:               0xc06660e58e7d3eed37b967986ed060be0f5cb67351cb4d9b2bf52ece2cca46ce4e523bbd83b48f8874c2aef59972ae3a35b319310e5fdfe43cbb72ba0e57050b1b
```


```
iexec order publish --app
? Using wallet developper_wallet
? Using wallet developper_wallet
Please enter your password to unlock your wallet [hidden]
? Do you want to publish the following apporder?
app:                0x814FCFf7aa640F3b59CADF8011F89B55D3De3368
appprice:           0
volume:             1000000
tag:                0x0000000000000000000000000000000000000000000000000000000000000000
datasetrestrict:    0x0000000000000000000000000000000000000000
workerpoolrestrict: 0x0000000000000000000000000000000000000000
requesterrestrict:  0x0000000000000000000000000000000000000000
salt:               0xe0fe46a67f63ce09a5e0e847f6615111733b25db3dfd3086b216f6410201a14e
sign:               0xc06660e58e7d3eed37b967986ed060be0f5cb67351cb4d9b2bf52ece2cca46ce4e523bbd83b48f8874
c2aef59972ae3a35b319310e5fdfe43cbb72ba0e57050b1b
 Yes
✔ apporder successfully published with orderHash 0x940b6be33f364ed4fa2d70e09451118d1e50433da5ced4d477e5c0dceb843610
```

## Buy a crypto coin analysis

From the marketplace, https://v3.market.iex.ec, this is possible to process a cloud coin analysis   
You only need the dataset and dapp addresses deployed just created, the markeplace is able to find the corresponding orders.

![buy a analysis](images/buy.png)

Information from CoinMarketCap is updated everyday, so dataset can be created daily without changing the existing application, the app has been designed to support updated datasets.

But it is strongly recommended to improve the application and provide improved analysis.

## Your daily report

your report contains a market report with a collection of plots    

![Candle stick](images/cancdlestick_chart_for_rlc.png)
![RoI](images/roi.png)

## Future work/next step:

 * Best prediction algorithm.
 * Use iExec security layers for data privacy.
