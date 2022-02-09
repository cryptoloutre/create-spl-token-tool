import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("\nPlease provide, with the following order, the network, the number of tokens to mint, the path to your private key and your public key!\n Veuillez renseigner, avec l'ordre suivant, le réseau, le nombre de tokens à mint, le chemin vers votre clé privée et votre clé publique !")
        exit()

    ### Create the needed variables from the user inputs ### 
    network = sys.argv[1]
    quantitytomint = sys.argv[2]
    path_keypair = sys.argv[3]
    pubkey = sys.argv[4]

    token_address = ""
    token_account = ""


    if network == "mainnet-beta" or network == "devnet":

        try:
            quantity = int(quantitytomint)

            ### Set the command to create a token ###
            create_token_cmd = f'spl-token create-token --url {network} --fee-payer {path_keypair} --mint-authority {pubkey}'

            ### Execute the command and get the output ###
            create_token_result = subprocess.check_output(create_token_cmd, shell=True, universal_newlines=True)

            ### Verify if the transaction succeed ###
            if "Signature:" in create_token_result:
                print("\nToken created!")

                ### Get the address of the token created from the output ###
                for i in range(15, 59):
                    token_address += create_token_result[i]

                ### Set the command to create the associated token account ###
                create_token_account_cmd = f'spl-token create-account --url {network} --fee-payer {path_keypair} --owner {pubkey} {token_address}'

                ### Execute the command and get the output ###
                create_token_account_result = subprocess.check_output(create_token_account_cmd, shell=True, universal_newlines=True)
                
                ### Verify if the transaction succeed ###
                if "Signature:" in create_token_account_result:
                    print("\nToken account created!")

                    ### Get the address of the associated token account from the output ###
                    for i in range(17, 61):
                        token_account += create_token_account_result[i]

                    ### Set the command to mint token ###
                    mint_token_cmd = f'spl-token mint --url {network} --fee-payer {path_keypair} --mint-authority {path_keypair} {token_address} {quantitytomint} {token_account}'
                    
                    ### Execute the command and get the output ###
                    mint_token_result = subprocess.check_output(mint_token_cmd, shell=True, universal_newlines=True)

                    ### Verify if the transaction succeed ###
                    if "Signature:" in mint_token_result:
                        print("\nToken minted!")

                        if network == "mainnet-beta":
                            url = f'https://solscan.io/token/{token_address}'

                        else:
                            url = f'https://solscan.io/token/{token_address}?cluster=devnet'

                        print(f'\nSee your token at this url : {url}')

        except ValueError:
            print("\nOops! It's not a valid number. Try again...")
    else:
        print("\nOops! It's not a valid network. Only mainnet-beta and devnet are allowed")
