# \# AWS Serverless Customer Feedback Platform

# 

# A fully serverless customer feedback platform built on AWS that collects customer feedback through a web application, performs sentiment analysis using Amazon Comprehend, stores the results in DynamoDB, sends real-time email alerts for negative feedback using Amazon SNS, and presents analytics through an interactive dashboard.

# 

# This project demonstrates the design and implementation of a modern serverless application using AWS managed services with a focus on scalability, automation, and cost efficiency.

# 

# \---

# 

# \## Architecture

# 

# ```

# &#x20;                       Customer

# &#x20;                           │

# &#x20;                           ▼

# &#x20;               Amazon S3 Static Website

# &#x20;                    (Feedback Form)

# &#x20;                           │

# &#x20;                           ▼

# &#x20;                     Amazon API Gateway

# &#x20;                           │

# &#x20;                           ▼

# &#x20;                   AWS Lambda Function

# &#x20;                  (process-feedback)

# &#x20;                ┌──────────┼───────────┐

# &#x20;                ▼          ▼           ▼

# &#x20;     Amazon Comprehend   DynamoDB     Amazon SNS

# &#x20;     Sentiment Analysis  Feedback     Email Alerts

# &#x20;                         Storage      (Negative Feedback)

# 

# &#x20;                           │

# &#x20;                           ▼

# &#x20;                     API Gateway (/stats)

# &#x20;                           │

# &#x20;                           ▼

# &#x20;                  AWS Lambda (get-stats)

# &#x20;                           │

# &#x20;                           ▼

# &#x20;              Amazon S3 Analytics Dashboard

# &#x20;                           │

# &#x20;                           ▼

# &#x20;                        Administrator

# ```

# 

# \---

# 

# \# Features

# 

# \- Customer feedback submission through a responsive web interface

# \- Static website hosting using Amazon S3

# \- REST API built with Amazon API Gateway

# \- Serverless backend using AWS Lambda

# \- Automatic sentiment analysis using Amazon Comprehend

# \- Named entity extraction

# \- Feedback storage in Amazon DynamoDB

# \- Real-time email notifications for negative feedback using Amazon SNS

# \- Interactive analytics dashboard

# \- Sentiment visualization using Chart.js

# \- Searchable feedback table

# \- CSV export functionality

# \- Designed for serverless scalability

# 

# \---

# 

# \# AWS Services Used

# 

# | Service | Purpose |

# |----------|---------|

# | Amazon S3 | Static website hosting |

# | API Gateway | REST API endpoints |

# | AWS Lambda | Backend business logic |

# | Amazon DynamoDB | Feedback storage |

# | Amazon Comprehend | Sentiment analysis \& entity extraction |

# | Amazon SNS | Email notifications for negative feedback |

# | IAM | Secure permissions management |

# | CloudWatch | Monitoring and logging |

# | GitHub | Source code management |

# 

# \---

# 

# \# Project Structure

# 

# ```

# aws-serverless-feedback-platform/

# 

# ├── frontend/

# │   └── index.html

# │

# ├── dashboard/

# │   └── index.html

# │

# ├── lambda/

# │   ├── process-feedback.py

# │   └── get-stats.py

# │

# ├── architecture/

# │   └── architecture.png

# │

# ├── screenshots/

# │   ├── feedback-page-screenshot.png

# │   ├── dashboard-page-screenshot.png

# │   ├── dynamodb-items-screenshot.png

# │   ├── cloudwatch-logs-screenshot.png

# │   └── SNS-email-screenshot.png

# │

# └── README.md

# ```

# 

# \---

# 

# \# API Endpoints

# 

# \## Submit Feedback

# 

# ```

# POST /feedback

# ```

# 

# Example Request

# 

# ```json

# {

# &#x20; "name": "John Doe",

# &#x20; "email": "john@example.com",

# &#x20; "message": "Great learning experience!"

# }

# ```

# 

# Example Response

# 

# ```json

# {

# &#x20; "success": true,

# &#x20; "sentiment": "POSITIVE"

# }

# ```

# 

# \---

# 

# \## Retrieve Analytics

# 

# ```

# GET /stats

# ```

# 

# Example Response

# 

# ```json

# {

# &#x20; "total": 25,

# &#x20; "sentiment\_breakdown": {

# &#x20;   "POSITIVE": 18,

# &#x20;   "NEGATIVE": 5,

# &#x20;   "NEUTRAL": 2

# &#x20; }

# }

# ```

# 

# \---

# 

# \# Data Flow

# 

# 1\. User submits feedback from the web application.

# 2\. Amazon API Gateway receives the request.

# 3\. AWS Lambda processes the request.

# 4\. Amazon Comprehend performs sentiment analysis.

# 5\. Named entities are extracted.

# 6\. Feedback is stored in DynamoDB.

# 7\. If the sentiment is NEGATIVE:

# &#x20;  - Amazon SNS sends an email notification.

# 8\. The analytics dashboard retrieves aggregated statistics through the `/stats` API.

# 

# \---

# 

# \# Dashboard

# 

# The analytics dashboard provides:

# 

# \- Total feedback received

# \- Sentiment distribution

# \- Top extracted entities

# \- Recent submissions

# \- Search functionality

# \- CSV export

# \- Interactive charts powered by Chart.js

# 

# \---

# 

# \# Security

# 

# \- IAM roles with least-privilege permissions

# \- CORS configured for API Gateway

# \- Serverless architecture with no exposed servers

# \- Secure communication using HTTPS endpoints

# \- Input validation within Lambda

# 

# \---

# 

# \# Screenshots

# 

# \## Feedback Form

# 

# !\[Feedback Form](screenshots/feedback-page-screenshot.png)

# 

# \---

# 

# \## Analytics Dashboard

# 

# \*(Insert screenshot here)\*

# 

# \---

# 

# \## DynamoDB Table

# 

# \*(Insert screenshot here)\*

# 

# \---

# 

# \## CloudWatch Logs

# 

# \*(Insert screenshot here)\*

# 

# \---

# 

# \## SNS Email Notification

# 

# \*(Insert screenshot here)\*

# 

# \---

# 

# \# Future Improvements

# 

# \- CloudFront CDN

# \- Route 53 custom domain

# \- AWS Certificate Manager (HTTPS)

# \- GitHub Actions CI/CD

# \- Authentication with Amazon Cognito

# \- User dashboard

# \- Feedback categorization

# \- Historical trend analysis

# \- AI-generated summaries using Amazon Bedrock

# 

# \---

# 

# \# Lessons Learned

# 

# This project provided hands-on experience with:

# 

# \- Designing serverless architectures

# \- Building REST APIs with API Gateway

# \- Developing Lambda functions in Python

# \- Integrating Amazon Comprehend

# \- Working with DynamoDB

# \- Managing IAM permissions

# \- Debugging distributed cloud applications

# \- Monitoring applications using CloudWatch

# \- Event-driven notifications with Amazon SNS

# \- Building static web applications hosted on Amazon S3

# 

# \---

# 

# \# Technologies

# 

# \- HTML5

# \- CSS3

# \- JavaScript

# \- Python

# \- Chart.js

# \- AWS Lambda

# \- Amazon S3

# \- API Gateway

# \- Amazon DynamoDB

# \- Amazon Comprehend

# \- Amazon SNS

# \- CloudWatch

# \- GitHub

# 

# \---

# 

# \# Author

# 

# \*\*Francis Ocran\*\*

# 

# Cloud Engineer | AWS Enthusiast

# 

# GitHub:

# https://github.com/Francis-Ocran-git

# 

# \---

# 

# \## License

# 

# This project is licensed under the MIT License.

