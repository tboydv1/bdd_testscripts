# Created by Oluwatobi Omotosho at 3/1/2021
Feature: Training Management
  As a user (admin, or user),
  I should have access to the Trainee Management Feature (Dashboard)
  based on my permissions

  Background:
    Given That I am on the login page
    When I enter my login details
    And I click on the login button
    Then System should redirect me to the dashboard

  Scenario: An admin I can view all trainees
    When Click on the trainees tab
    Then System should display trainees page
    And Display record of existing trainees


  Scenario: An admin can send an invite to a trainee
    Given That I am on the trainees page
    When I click on the invite button
    And I add email to the provided field
    And I click on the send invite button
    Then System should display an success page


  Scenario: An Admin can assign courses to a trainee
    Given That I am on the trainees page
    And I have selected a trainee
    When I click on the Assign course action
    And I select a course
    And click the Assign course button
    Then System should display a success message

  Scenario: An Admin can create a group
    Given That I am on the groups page
    When I click on the create group button
    And I Select or enter group name
    Then System creates group successfully
    And Group is added to list of existing groups
