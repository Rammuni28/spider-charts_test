from django.db import models

from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class StCompanyOverview(Base):
    __tablename__ = 'st_company_overview'
    
    st_company_id = Column(Integer, primary_key=True, autoincrement=True)
    st_company_name = Column(String(255), nullable=False)
    st_company_description = Column(String(255), nullable=False)
    st_year_of_incorporation = Column(Date, nullable=False)
    st_country = Column(String(255), nullable=False)
    st_total_founders = Column(Integer, nullable=False)
    st_no_of_employees = Column(String(255), nullable=False)
    st_founder_names = Column(String(255), nullable=False)
    st_industry_type = Column(String(255), nullable=False)
    st_geography = Column(String(255), nullable=False)
    st_created_by = Column(Integer, default=1)
    st_modified_by = Column(Integer, default=1)
    st_created_on = Column(DateTime, default=func.current_timestamp())
    st_modified_on = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, default=True)
    
    funding_valuation = relationship("StFundingValuation", back_populates="company")
    ownership_structures = relationship("StOwnershipStructure", back_populates="company")
    parametric_scoring = relationship("StParametricScoring", back_populates="company")

class StFundingValuation(Base):
    __tablename__ = 'st_funding_valuation'
    
    st_funding_id = Column(Integer, primary_key=True, autoincrement=True)
    st_company_id = Column(Integer, ForeignKey('st_company_overview.st_company_id'), nullable=False)
    st_stage = Column(String(255), nullable=False)
    st_raised_to_date = Column(String(255), nullable=False)  # Changed to String
    st_last_valuation = Column(String(255), nullable=False)  # Changed to String
    st_current_valuation = Column(String(255), nullable=False)  # Changed to String
    st_capital_requirements = Column(String(255), nullable=False)  # Changed to String
    st_currency = Column(String(10), nullable=False, default='USD')  # New single currency column
    st_created_by = Column(Integer, default=1)
    st_modified_by = Column(Integer, default=1)
    st_created_on = Column(DateTime, default=func.current_timestamp())
    st_modified_on = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, default=True)
    
    company = relationship("StCompanyOverview", back_populates="funding_valuation")
class StOwnershipStructure(Base):
    __tablename__ = 'st_ownership_structure'
    
    st_ownership_id = Column(Integer, primary_key=True, autoincrement=True)
    st_company_id = Column(Integer, ForeignKey('st_company_overview.st_company_id'), nullable=False)
    st_type = Column(String(255), nullable=False)
    st_shareholder_name = Column(String(255), nullable=False)
    st_holding_percentage = Column(DECIMAL(5, 2), nullable=False)
    st_created_by = Column(Integer, default=1)
    st_modified_by = Column(Integer, default=1)
    st_created_on = Column(DateTime, default=func.current_timestamp())
    st_modified_on = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, default=True)
    
    company = relationship("StCompanyOverview", back_populates="ownership_structures")

class StParametricScoring(Base):
    __tablename__ = 'st_parametric_scoring'
    
    st_parametric_scoring_id = Column(Integer, primary_key=True, autoincrement=True)
    st_company_id = Column(Integer, ForeignKey('st_company_overview.st_company_id'), nullable=False)
    st_market_potential = Column(Integer, nullable=False)
    st_product_viability = Column(Integer, nullable=False)
    st_financial_health = Column(Integer, nullable=False)
    st_team_strength = Column(Integer, nullable=False)
    st_competitive_advantage = Column(Integer, nullable=False)
    st_customer_traction = Column(Integer, nullable=False)
    st_risk_factors = Column(Integer, nullable=False)
    st_exit_potential = Column(Integer, nullable=False)
    st_innovation = Column(Integer, nullable=False)
    st_sustainability = Column(Integer, nullable=False)
    st_created_by = Column(Integer, default=1)
    st_modified_by = Column(Integer, default=1)
    st_created_on = Column(DateTime, default=func.current_timestamp())
    st_modified_on = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_active = Column(Boolean, default=True)
    
    company = relationship("StCompanyOverview", back_populates="parametric_scoring")
