разработка бд для риэлторского агенства

Таблица сотрудников (агенты и администраторы)
id|full_name|phone| email |position| commission_rate| is_active| created_at 

Таблица клиентов
id | full_name |phone email|  passport_data| notes|  created_at T

Таблица объектов недвижимости
id| address| city| district |property_type| rooms| total_area| floor| total_floors| price| description| owner_id| agent_id| status| created_at| updated_at|

Таблица заявок от клиентов
id| client_id| agent_id|request_type| property_type| min_price| max_price| min_rooms| district |status| notes |created_at 

Таблица сделок
id| deal_number| property_id| buyer_id| seller_id| agent_id| deal_type| deal_date| deal_amount| commission_amount| contract_number| status| created_at

Таблица просмотров объектов
id |property_id| client_id| agent_id| viewing_date| duration_minutes| client_feedback| created_at 

Таблица задач
id |title| description| assigned_to| due_date| priority| status| related_deal_id |created_at 
