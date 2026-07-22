Feature: Leave review
    @TestCaseKey=SCRUM-T11
    Scenario: Leave review
        
        Product Review System
          As a customer who recently purchased a product
          I want to leave a review
          So that I can share my feedback with other buyers
        
        Successfully leaving a review for a delivered item
            Given items paid for
            And items delivered
            When the user navigates to the order history page
            And selects the option to leave a review for the purchased item
            And provides a star rating and a written comment
            And submits the review
            Then the review should be successfully saved
            And the user should see a confirmation message "Thank you for your review!"
            And the review should be visible on the product's review page