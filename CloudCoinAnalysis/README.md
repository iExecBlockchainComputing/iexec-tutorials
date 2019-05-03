# CloudCoinAnalysis


Analysis of the 3 main cryptocurrencies offering a cloud computing solution or similar: golem, sonm and iexec   


The application runs on top of iExec platform and generate a market report, it performs exploratory data analysis
and builds machine learning models to predict market prices in future 30 days for the above 3 cryptocurrencies.

About iExec:

iExec is building the future of the Internet infrastructure by decentralizing the cloud computing market. It is the first blockchain-based cloud computing marketplace.
The iExec network connects cloud resource sellers with cloud resource buyers, encouraging an ecosystem of decentralized and autonomous, privacy-preserving applications.
This network aims at providing companies with scalable, secure and easy access to the services, datasets and computing resources they need. iExec’s technology relies on Ethereum smart contracts and allows for a virtual cloud infrastructure that provides high-performance computing services on-demand.


Source:
The code is derivated from:

* https://github.com/jieyima/Cryptocurrency_Investment_Analysis_and_Modeling for the analysis part

* https://github.com/JesseVent/crypto for the building dataset


##Building datasets:

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

### Register the dataset in the blockchain

Let's register the access to the dataset, the dataset is not store in ethereum, only access and managament.

```
iexec dataset init  
```
Edit the dataset info in iexec.json file
The path to dataset must public and accessible from anywere.  

The checksum will be use to check the integrity on the file (not implemented).

```
"dataset": {
  "owner": "0x9CdDC59c3782828724f55DD4AB4920d98aA88418",
  "name": "cloincoin-20190502-dataset",
  "multiaddr": "https://raw.githubusercontent.com/iExecBlockchainComputing/apps/master/CloudCoinAnalysis/dataset/cloudcoin_2019-05-02.zip",
  "checksum": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```

```
iexec dataset deploy
ℹ using chain [kovan]
? Using wallet data_owner_wallet
Please enter your password to unlock your wallet [hidden]
✔ Deployed new dataset at address 0xFCE3F07D96b0f2458Bb82868087AcAE636232B4E
```

###Publish selling order for the dataset.

As the dataset is now registered ad ownership is store on the blockchain; the owner has to publish an order defining the price, the volume and restrictions for the usage of the dataset.

```
iexec order init --dataset
```

Let's create an order with price at  10 nRLC and a volume of 1000 tasks, with no extra restriction.
The dataset has no usage restriction for user, worker pool and app.

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
iexec order publish --dataset --wallet-file data_owner_wallet
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



Future work:
