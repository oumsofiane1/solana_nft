### dstool
to run this command just use
```
python dstool.py <pathToFile> --tag="Eyes=Blue Skull Glasses" >> mints.txt
```

then to extract the holders you can just run 
```
python owners.py <pathToFile> <path to mint file previous generated> --data=owner_wallet
```

exact steps for the current data:
```
python dstool.py data/mint-data.json --tag="Stamp=NICE-YES" --data=tokenMetadata.mint >> mints.txt
python owners.py data/metaboss-all.json mints.txt  --data=owner_wallet >> holders.csv
```
