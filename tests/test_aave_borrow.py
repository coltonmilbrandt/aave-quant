from scripts.aave_borrow import (
    get_asset_price,
    repay_all,
    get_borrowable_data,
    approve_erc20,
    get_lending_pool,
)

from scripts.helpful_scripts import (
    get_account
)

from brownie import config, network
from web3 import Web3

def test_get_asset_price():
    # Arrange
    dai_eth_price = get_asset_price(config["networks"][network.show_active()]["dai_eth_price_feed"])
    # Act

    # Assert
    assert dai_eth_price > 0

def test_repay_all():
    # Arrange

    # Act

    # Assert
    
    pass

def test_get_borrowable_data():
    # Arrange

    # Act

    # Assert
    
    pass

def test_approve_erc20():
    # Arrange
    account = get_account()
    amount = 1000000000000000000000000000000000
    lending_pool = get_lending_pool()
    # Act
    tx = approve_erc20(
        amount,
        lending_pool,
        config["networks"][network.show_active()]["dai_token"],
        account,
    )
    # Assert
    assert tx is not True

def test_get_lending_pool():
    # Arrange
    # Act
    lending_pool = get_lending_pool()
    # Assert
    assert lending_pool is not None