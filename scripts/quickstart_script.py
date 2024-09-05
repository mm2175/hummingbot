from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


class QuickstartScript(ScriptStrategyBase):
    markets = {"binance_paper_trade": {"BTC-USDT", "ETH-USDT"}}

    def on_tick(self):
        price = self.connectors['binance_paper_trade'].get_mid_price("BTC-USDT")
        msg = f"Bitcoin price ${price}"
        self.logger().info(msg)
        self.notify_hb_app(msg)
