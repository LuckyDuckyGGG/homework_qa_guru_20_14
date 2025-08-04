<h1 align="centre"> Автоматизированные UI-тесты AR Mobile</h1>

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.34.2-green.svg)
![Allure](https://img.shields.io/badge/allure-2.15.0-orange.svg)

## 📌 О проекте

Автоматизированные тесты для веб-интерфейса образовательной платформы, покрывающие:
- Авторизацию пользователей по ролям (Владелец, Администратор, Инспектор, Подрядчик, Наблюдатель, Супервизор)
- Создание проекта под ролью (Владелец)
- Невозможность создать проект под ролями (Администратор, Инспектор, Подрядчик, Наблюдатель, Супервизор)

## 🛠 Технологический стек

- **Python** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Selene** - удобная обертка над Selenium
- **Pytest** - фреймворк для тестирования
- **Allure** - генератор отчетов
- **Allure TestOps** - генерация тестовой документации
- **Jenkins** - система непрерывной интеграции
- **Selenoid** - контейнеризованный запуск браузеров

## 🌐 CI/CD и Мониторинг

### <img src="https://jenkins.io/images/logos/jenkins/jenkins.svg" width="20"> **Jenkins Pipeline**

**Ссылка на сборку**:  
[**AR Mobile UI Job**](https://jenkins.autotests.cloud/job/LuckyDucky_qa_guru_python_20_14_jenkins/)

**Особенности пайплайна**:
- Запуск тестов с использованием браузера в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram
- Генерация тестовой документации в Allure TestOps

### <img src="https://arm.vr-arsoft.com/faviconARM.ico" width="20"> AR Mobile  
**Пример прохождения тестов**  
![Test image](https://github.com/LuckyDuckyGGG/homework_qa_guru_20_14/blob/main/files/45a9ea735ec8f2ee.png)   
![Test video](https://luckyduckyggg.github.io/homework_qa_guru_20_14/)

### <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="20"> Allure Report
**Пример отчёта**:  
[**AR Mobile UI Report**](https://jenkins.autotests.cloud/job/LuckyDucky_qa_guru_python_20_14_jenkins/1/allure/)

![Report image](https://github.com/LuckyDuckyGGG/homework_qa_guru_20_14/blob/main/files/chrome_2swgE3tEru.png)  
![Report image2](https://github.com/LuckyDuckyGGG/homework_qa_guru_20_14/blob/main/files/chrome_eiUxsOyLQM.png)

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Пример отчета от telegram бота**:  
![Telegram bot image](https://github.com/LuckyDuckyGGG/homework_qa_guru_20_14/blob/main/files/Telegram_GaiX5vOHET.png)

### <img src="https://allure.autotests.cloud/favicon.ico" width="20"> Allure TestOps
**Пример тестовой документации**:  
![Allure TestOps image](https://github.com/LuckyDuckyGGG/homework_qa_guru_20_14/blob/main/files/chrome_ElEmi8HIuI.png)