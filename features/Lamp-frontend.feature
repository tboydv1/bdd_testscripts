# Created by Oluwatobi Omotosho at 3/1/2021
Feature: Training Management
  As a user (admin, or user),
  I should have access to the Trainee Management Feature (Dashboard)
  based on my permissions

  Background:
    Given I am logged in as an admin on lamp-frontend
    When I click the Trainees tab
    Then I should see the Trainees page and all Trainees


  Scenario: An admin can access the Trainee Tab
    When I search for the for the logged in user
    Then user should be found
    And role should be HR

  Scenario: An admin can send an invite
    When I click the invite button
    Then I should see the invite Trainees dialog
    When I insert an email
    And I click the Add button
    Then I should be able to add the email successfully
    When I click the send invite button
    Then System displays an invite send modal

