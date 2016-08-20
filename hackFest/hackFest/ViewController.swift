//
//  ViewController.swift
//  hackFest
//
//  Created by Vicky Wang on 2016-08-20.
//  Copyright © 2016 Vicky Wang. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBAction func price1(sender: UIButton) {
        restaurants.text = "McDonald’s, Tim Hortons, Dailo, 259 Host"
    }
    
    @IBAction func price2(sender: UIButton) {
        restaurants.text = "McDonald’s, Tim Hortons, Jack Astor, Milestone, Dailo, Little India, 259 Host, Crepes Club"
    }
    
    @IBAction func price3(sender: UIButton) {
        restaurants.text = "McDonald’s, Tim Hortons, Jack Astor, America Restaurant, Milestone, Dailo, Thai Kitchen, Little India, Banjara, 259 Host, Amber, Crepes Club"
    }
    
    @IBAction func price4(sender: UIButton) {
        restaurants.text = "McDonald’s, Tim Hortons, Jack Astor, Trump, America Restaurant, Milestone, Dailo, Thai Kitchen, Ki Restaurant, Little India, Banjara, 259 Host, Amber, Crepes Club, Europe Bar"
    }
    
    @IBOutlet weak var restaurants: UILabel!
    
    
    @IBAction func downtown(sender: UIButton) {
        restaurantDemo.text = "Trump, Little India, Crepes Club"
    }
    
    @IBAction func west(sender: UIButton) {
        restaurantDemo.text = "Tim Hortons, Milestone, Ki Restaurant, 259 Host"
    }
    
    @IBAction func east(sender: UIButton) {
        restaurantDemo.text = "Jack Astor, Dailo, Banjara, Europe Bar"
    }
    
    @IBAction func north(sender: UIButton) {
        restaurantDemo.text = "McDonald’s, America Restaurant, Thai Kitchen, Amber"
    }
    
    @IBOutlet weak var restaurantDemo: UILabel!
    
    
    @IBAction func fastfood(sender: UIButton) {
        restaurantType.text = "McDonald’s, Tim Hortons"
    }
    
    @IBAction func american(sender: UIButton) {
        restaurantType.text = "Jack Astor, Trump, America Restaurant, Milestone"
    }
    
    @IBAction func asian(sender: UIButton) {
        restaurantType.text = "Dailo, Thai Kitchen, Ki Restaurant"
    }
    @IBAction func indian(sender: UIButton) {
        restaurantType.text = "Little India, Banjara, 259 Host"
    }
    
    @IBAction func european(sender: UIButton) {
        restaurantType.text = "Amber, Crepes Club, Europe Bar"
    }
    
    @IBOutlet weak var restaurantType: UILabel!
    
    @IBAction func yes(sender: UIButton) {
        restaurantDiet.text = "McDonald’s, Jack Astor, Trump, America Restaurant, Thai Kitchen, Ki Restaurant, Banjara, 259 Host, Crepes Club, Europe Bar"
    }
    @IBAction func no(sender: UIButton) {
        restaurantDiet.text = "McDonald’s,Tim Hortons, Jack Astor, Trump, America Restaurant, Milestone, Dailo, Thai Kitchen, Ki Restaurant, Little India, Banjara, 259 Host, Amber, Crepes Club, Europe Bar"
    }
    
    @IBOutlet weak var restaurantDiet: UILabel!
    
    
    @IBAction func restaurant1(sender: UISlider) {
        let restaurant1 = lroundf(sender.value)
        rating1.text = "\(restaurant1)"
    }
    
    @IBOutlet weak var rating1: UILabel!
    
    @IBAction func restaurant2(sender: UISlider) {
        let restaurant2 = lroundf(sender.value)
        rating2.text = "\(restaurant2)"
    }
    @IBOutlet weak var rating2: UILabel!
    
    @IBAction func restaurant3(sender: UISlider) {
        let restaurant3 = lroundf(sender.value)
        rating3.text = "\(restaurant3)"
    }
    
    @IBOutlet weak var rating3: UILabel!
    
    
    @IBOutlet weak var signupEmail: UITextField!
    
    @IBOutlet weak var setPassword: UITextField!
    
    @IBOutlet weak var confirmPassword: UITextField!
    
    @IBAction func signUp(sender: UIButton) {
        self.signupEmail.resignFirstResponder()
        self.setPassword.resignFirstResponder()
        self.confirmPassword.resignFirstResponder()
    }
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        self.view.endEditing(true)
    }
    
    @IBOutlet weak var email: UITextField!
    @IBOutlet weak var password: UITextField!
    
    @IBAction func logIn(sender: UIButton) {
        self.email.resignFirstResponder()
        self.password.resignFirstResponder()
    }
    
    @IBAction func recommendationSlider(sender: UISlider) {
        let recommendationSlider = lroundf(sender.value)
        recommendationRating.text = "\(recommendationSlider)"
        
    }
    @IBOutlet weak var recommendationRating: UILabel!
    
    @IBOutlet weak var restaurantName: UITextField!
    
    @IBOutlet weak var comment: UITextField!
    
    @IBAction func addRecommendation(sender: UIButton) {
        self.restaurantName.resignFirstResponder()
        self.comment.resignFirstResponder()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

