# Created by Oluwatobi Omotosho at 3/1/2021
Feature: Training Management
  As a user (admin, or user),
  I should have access to the Trainee Management Feature (Dashboard)
  based on my permissions


  Scenario: An admin can access the Trainee Tab
    Given I am logged in as an admin on lamp-frontend
    When I click the Trainees tab
    Then I should see the Trainees page