from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# 01
# class InsufficientBalanceException(Exception):
#     def __init__(self, balance: float):
#         self.balance = balance

# @app.exception_handler(InsufficientBalanceException)
# async def insufficient_balance_handler(request, exc):
#     return JSONResponse(
#         status_code=403,
#         content={"error": "Forbidden", "message": "Insufficient balance", "current_balance": exc.balance},
#     )


# @app.get("/withdraw/{amount}")
# def withdraw(amount: float):
#     balance = 100.0
#     if amount > balance:
#         raise HTTPException(status_code=400)
#         # raise InsufficientBalanceException(balance)
#     return {"message": "Withdrawal successful", "new_balance": balance - amount}

# 02
# Custom Exception for Database Connection Issues
class DatabaseNotFoundException(Exception):
    def __init__(self, database_name: str):
        self.database_name = database_name

# Global Exception Handler for DatabaseNotFoundException
@app.exception_handler(DatabaseNotFoundException)
async def database_not_found_handler(request, exc):
    return JSONResponse(
        status_code=503,  # 503 Service Unavailable
        content={"error": "Service Unavailable", "message": f"Database '{exc.database_name}' is currently unavailable"},
    )

# Simulated Route that Raises DatabaseNotFoundException
@app.get("/database-status")
def check_database():
    db_available = False  # Simulating a database outage
    if not db_available:
        raise DatabaseNotFoundException("PostgreSQL")  # Raise exception
    return {"message": "Database is operational"}

