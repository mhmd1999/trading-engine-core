from abc import ABC, abstractmethod

# این یک Interface است که ما رو از وابستگی به ORM جنگو نجات میده
class TradeRepository(ABC):
    @abstractmethod
    def get_user_trades(self, user_id):
        pass

    @abstractmethod
    def save_trade(self, trade_data):
        pass
