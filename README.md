# create-spl-token-tool

# English version

Python script to faciliate the creation of token on the Solana blockchain (SPL Tokens). In fact, you just have to run one command to create a token instead of the multiple commands if you use the `spl-token` command-line utility directly from a terminal.

Donations can be made at `6MupHwVuaZnxeXbw2DEvH96ouaWdg5TygPaSruB4H7YG` if you are feeling generous!

## Prerequisites

* `spl-token` command-line utility. Once you have [Rust installed](https://rustup.rs/), run:  
  
   `cargo install spl-token-cli`
* A keypair file with an associated public key funded. Follow the [Solana documentation](https://docs.solana.com/wallet-guide/file-system-wallet) to get one.
   
## Installation

1. Clone the repo :  
  
    `git clone https://github.com/cryptoloutre/create-spl-token-tool.git`
  
2. Change directory and run :  
  
    ```
    cd create-spl-token-tool
    python create-spl-token.py <NETWORK> <TOKEN_NUMBER> <KEYPAIR> <PUBKEY> <DECIMALS_NUMBER> <MINT_AUTHORITY_OPTION>
    ```
  
  With:  
  * `<NETWORK>` : network on wich you want to create a token (`mainnet-beta` or `devnet`)
  * `<TOKEN_NUMBER>` : number of token you want to mint
  * `<KEYPAIR>` : path of your keypair file
  * `<PUBKEY>` : your public key (Must be the address associated to the keypair file)
  * `<DECIMALS_NUMBER>` : number of decimals of your token (By default, SPL-token has 9 decimals)
  * `<MINT_AUTHORITY_OPTION>` : if you want to disable future token mint set to `disable`, set to `enable` otherwise

## Community
If you have questions or any troubles, feel free to reach me on Twitter [@laloutre](https://twitter.com/laloutre).

# Version Française

Script Python qui a pour but de faciliter la création de token sur la blockchain Solana (SPL Tokens). En effet, vous aurez juste à éxecuter une ligne de commande au lieu des nombreuses lignes de commande si vous utilisez directement l'utilitaire de ligne de commande `spl-token` depuis un terminal.

Des dons peuvent être faits à `6MupHwVuaZnxeXbw2DEvH96ouaWdg5TygPaSruB4H7YG` si vous vous sentez généreux !

## Prérequis

* l'utilitaire de ligne de commande `spl-token`. Une fois que vous avez [Rust installé](https://rustup.rs/), exécutez:  
  
   `cargo install spl-token-cli`
* Un fichier keypair avec des $SOL dessus. Suivez la [documentation de Solana](https://docs.solana.com/wallet-guide/file-system-wallet) ou mon [GitBook](https://laloutre.gitbook.io/creer-un-token-sur-la-blockchain-solana/installation-des-outils-necessaires/1.-solana-tools-et-wallet#_ref91180889) pour en créer un.
   
## Installation

1. Cloner le repo :   
  
    `git clone https://github.com/cryptoloutre/create-spl-token-tool.git`
  
2. Changer de répertoire et exécuter :  
  
    ```
    cd create-spl-token-tool
    python create-spl-token.py <NETWORK> <TOKEN_NUMBER> <KEYPAIR> <PUBKEY> <DECIMALS_NUMBER> <MINT_AUTHORITY_OPTION>
    ```
  
  Avec:  
  * `<NETWORK>` : réseau sur lequel vous souhaitez créer un token (`mainnet-beta` ou `devnet`)
  * `<TOKEN_NUMBER>` : nombre de tokens à créer
  * `<KEYPAIR>` : chemin d'accès vers votre fichier keypair
  * `<PUBKEY>` : votre clé publique (Doit être l'adresse associée au fichier keypair)
  * `<DECIMALS_NUMBER>` : nombre de déciamles de votre token. (Par défaut, les SPL-tokens ont 9 décimales)
  * `<MINT_AUTHORITY_OPTION>` : si vous voulez désactiver le mint de futurs tokens, fixez la valeur à `disable`. Fixez la valeur à `enable` sinon.

## Communauté
Si vous avez des questions ou des problèmes, n'hésitez pas à me contacter sur Twitter [@laloutre](https://twitter.com/laloutre).
