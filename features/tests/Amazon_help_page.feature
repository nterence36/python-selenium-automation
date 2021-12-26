# Created by ntere at 12/25/2021
Feature: Test for amazon terms and conditions


  Scenario: User can open and close Amazon Privacy Notice

     Given Open Amazon T&C page
     When Store original windows
     And Click on Amazon Privacy Notice link
     And Switch to the newly opened window
     Then Verify Amazon Privacy Notice page is opened
     And User can close new window
     Then Return the original window
