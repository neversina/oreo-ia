# Frontend Dockerfile (assumes a React/Vue app that outputs a build directory)
FROM node:18-alpine AS build

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Serve with a lightweight static server
FROM node:18-alpine
RUN npm install -g serve
WORKDIR /app
COPY --from=build /app/build /app/build
EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
