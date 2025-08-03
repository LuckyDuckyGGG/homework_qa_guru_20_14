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
- **Jenkins** - система непрерывной интеграции
- **Selenoid** - контейнеризованный запуск браузеров

## 🌐 CI/CD и Мониторинг

### <img src="https://jenkins.io/images/logos/jenkins/jenkins.svg" width="20"> **Jenkins Pipeline**

**Ссылка на сборку**:  
[]()

**Особенности пайплайна**:
- Запуск тестов в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram

### <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="20"> Allure Report
**Пример отчёта**:  

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Бот для уведомлений**:  