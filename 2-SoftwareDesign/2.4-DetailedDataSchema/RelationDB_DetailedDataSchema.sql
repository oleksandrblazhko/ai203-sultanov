drop table USER CASCADE;
drop table SELF-ESTEEM DEVELOPMENT COMPLEX CASCADE;
drop table AIR CLEANNESS CASCADE;
drop table EQIPMENT INDICATORS CASCADE;
drop table HYDROMETEROLOGICAL CENTER CASCADE; 

CREATE TABLE USER( --користувач
user_id INT PRIMARY KEY, -- id
name VARCHAR (20), -- ПІБ
photo BINARY(1) -- зображення
email NUMBER(4), -- N email адреси співробітника
self_est_complex_id INT REFERENCES SELF-ESTEEM DEVELOPMENT COMPLEX(self_est_complex_id),-- id комлексу самоповаги
air_clean_id INT PREFERENCES AIR CLEANNESS(air_clean_id) -- id чистоти повітря
);

CREATE TABLE SELF_ESTEEM_DEVELOPMENT_COMPLEX( --комплекс самоповаги
self_est_complex_id INT PRIMARY KEY, -- id
title VARCHAR(40), -- назва комплексу
content VARCHAR(100), -- опис комплексу
Link VARCHAR (50) -- посилання на комплекс самоповаги
);

CREATE TABLE AIR_CLEANNESS( --чистота повітря
air_clean_id INT PRIMARY KEY, -- id
dust_amount NUMBER(20) -- кількість пилу у повітрі
);

CREATE TABLE EQUIPMENT_INDICATORS( -- показники обладнання
equip_indicators_id INT PRIMARY KEY, -- id
air_cleanness NUMBER(20) -- показник чистоти повітря
air_humidity NUMBER(20) -- показник вологості повітря
air_clean_id INT PREFERENCES AIR CLEANNESS(air_clean_id) -- id чистоти повітря
);

 
CREATE TABLE HYDROMETEROLOGICAL_CENTER( -- гідрометеорологічний центр
hydr_metr_centr_id INT PRIMARY KEY, -- id
changes_in_indicators NUMBER(20), -- зміни показників обладнання
);

