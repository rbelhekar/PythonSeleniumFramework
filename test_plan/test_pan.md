# Test Plan - Banking QA Automation

## 1. Objective
To validate the core functionalities of a banking web application, including login, account operations, fund transfer, and transaction history, using manual and automated testing.

## 2. Scope
### ✅ In Scope
- User Login / Logout
- Account Overview
- Fund Transfer
- Transaction History
- Error Handling

### ❌ Out of Scope
- Backend/Database testing
- Performance/Load testing

## 3. Test Types
- Manual Testing (initially)
- Automated Testing using Selenium + PyTest
- Regression Testing
- Smoke Testing
- CI/CD Integration via Jenkins

## 4. Tools & Tech
- **Automation**: Selenium, PyTest, Python
- **Test Management**: Excel / Notion / Markdown
- **Version Control**: Git + GitHub
- **CI/CD**: Jenkins
- **Browser**: Chrome (via ChromeDriver)

## 5. Risks
- Third-party demo website can break unexpectedly
- No access to DB means only front-end testing
- Network or browser update issues

## 6. Timeline
| Phase                | Status     |
|---------------------|------------|
| Setup & Planning     | ✅ Done     |
| Manual Test Design   | 🔄 In Progress |
| Automation Structure | 🔜 Next     |
| Writing Test Cases   | 🔜         |
| GitHub Integration   | 🔜         |
| CI/CD (Jenkins)      | 🔜         |
