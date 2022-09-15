# CenterSiberian
'api/v1/typelist' Возможность получить всех типов новостей по GET и добавление типа новостей по POST
'api/v1/typelist/<int:pk>/' Возможность получить конкретного типа GET, редактирование типа PUT, Удаление DELETE  (CRUD)
'api/v1/newlist' Возможность получить всех новостей по GET и добавление новостей по POST
'api/v1/newlist/<int:pk>/' Возможность получить конкретную новость GET, редактирование новости PUT, Удаление DELETE (CRUD)
'api/v1/newlistwithtypecolor' Возможность получить список всех новостей (имя, краткое описание, имя типа, цвет типа) GET;
'api/v1/newlistwithtype/<int:pk>/' Возможность получить список новостей определенного типа GET с ID.

required
Django              4.1.1
djangorestframework 3.13.1
pip                 21.3.1
