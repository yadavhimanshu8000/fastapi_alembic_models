import enum
from sqlalchemy import Column, Integer, String , DateTime, func , JSON, Float, Date ,ForeignKey 
from sqlalchemy.orm import relationship 
from .db import Base
from enum import Enum


class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_email = Column(String, unique=True, index=True)
    mobile_no = Column(Integer, nullable=False)
    password = Column(String,index=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now()) 
    
    payments = relationship("Payment", back_populates="user")



class Game_center(Base):
    __tablename__ ="game_center"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String , nullable=False)
    area = Column(String,nullable=False)
    city = Column(String, nullable=False)
    price_per_hours = Column(Float)
    discount_price = Column(Float)
    games = Column(String, index=True, nullable=False)
    food_items = Column(JSON,nullable=False)
    cold_drink = Column(JSON,nullable=False)
    create_time = Column(DateTime(timezone=True),server_default=func.now())
    
    specs = relationship("specs", back_populates="game_center")
    tournaments = relationship("Tournament", back_populates="game_center")
    payments = relationship("Payment", back_populates="game_center") 
    
   

class specs(Base):
    __tablename__ = "specs"
    
    id = Column(Integer,primary_key=True,index=True)
    pc_specs = Column(JSON)
    console_specs = Column(JSON,nullable=False)
    select_date = Column(String,nullable=False)
    select_time_slot= Column(String, nullable=False)
    number_of_available_slot = Column(Integer, nullable=False)
    notes = Column(String, nullable=False)
    create_time = Column(DateTime(timezone=True),server_default=func.now())
    
    game_center_id = Column(Integer, ForeignKey("game_center.id"))
    game_center = relationship("Game_center", back_populates="specs")
    

    
class Games_type(enum.Enum):
    pc_game = "PC_Games"
    console = "Console_Games"
    Simulator = "Simulator"
    Ar-Vr = "AR/VR"
    
class Game_available(Base):
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(Games_type), nullable=False)
    game_name = Column(String,nullable=False)
      
    

class Tournament(Base):
    __tablename__ = 'tournaments'
    
    id = Column(Integer,primary_key=True,index=True)
    date = Column(Date,nullable=False)
    format = Column(String,nullable=False)
    game_title = Column(String,nullable=False)
    hosted_by = Column(String,nullable=False)
    total_slots = Column(Integer,nullable=False)
    left_slots = Column(Integer,nullable=False)
    price_pool = Column(Float,nullable=False)
    create_at = Column(DateTime(timezone=True),server_default=func.now())
    game_center_id = Column(Integer, ForeignKey("game_center.id"))
    
    game_center = relationship("Game_center", back_populates="tournaments")



class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    game_center_id = Column(Integer, ForeignKey("game_center.id"))
    game_center_fee = Column(String,nullable=False)
    platform_fee = Column(Float, default=0.0)
    tax = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    payment_time = Column(DateTime(timezone=True), server_default=func.now())
    booking_time = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="payments")
    game_center = relationship("Game_center", back_populates="payments")
    
 
    
class Vendor_game_centre(Base):
    __tablename__ = "vendor_centre"
    
    id = Column(Integer, primary_key=True, nullable=True , index= True)
    game_center_name = Column(String, nullable=False)
    game_center_img = Column(String, nullable=False)
    discounted = Column(Float,nullable=False)
    price = Column(Float,nullable=False)
    today_timing = Column(String,nullable=False)
    total_slots = Column(Integer,nullable=False)
    address = Column(String,nullable=False)
    near_by_games = Column(String,nullable=False)
    area = Column(String,nullable=False)
    city = Column(String,nullable=False)
    pc_specs = Column(JSON,nullable=False)
    console_specs = Column(JSON,nullable=False)
    game_type = Column(String, nullable= False)
    game_name = Column(String, nullable= False)
    Facilities = Column(String,nullable=False)
    image = Column(String,nullable=False)
    
        
    

    
    


    
    
    
  

    

    
    
    
    
    
    
    
   
    
    
    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    














   






    
    
    
    
    
    
    
    
    
    

    
    
     
    
    
    
    
    