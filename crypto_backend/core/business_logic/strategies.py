# core/business_logic/strategies.py

class TradingStrategy(ABC):
    @abstractmethod
    def execute(self, market_data):
        pass

class QLearningStrategy(TradingStrategy):
    def execute(self, market_data):
        # منطق یادگیری تقویت‌شده اینجا قرار می‌گیره
        return "Buy/Sell Signal"

class SimpleMovingAverageStrategy(TradingStrategy):
    def execute(self, market_data):
        return "Hold"
