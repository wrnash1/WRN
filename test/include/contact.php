    <!-- BLOCK DIV START -->
    <div class="container text-white">
      <div class="row">
        <h4>Student Information</h4>
        <hr />

        <!-- FORM DIV START -->
        <div id="form-div">
          <form class="was-validated">
            <div class="form-row">
              <div class="col">
                <label for="first_name">First Name:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="first_name" placeholder="First Name" required />
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="last_name">Last Name:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="last_name" placeholder="Last Name" required />
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="address">Street Address:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="address" placeholder="Address Line 1" required />
                <input class="form-control" type="text" name="address" placeholder="Address Line 2" style="margin-top: 1.5em" />
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="city">City:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="city" placeholder="City" required />
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="state">State:</label>
              </div>
              <div class="col">
                <select class="form-control" id="state" required>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="DC">District Of Columbia</option>
                  <option value="FL">Florida</option>
                  <option value="GA">Georgia</option>
                  <option value="HI">Hawaii</option>
                  <option value="ID">Idaho</option>
                  <option value="IL">Illinois</option>
                  <option value="IN">Indiana</option>
                  <option value="IA">Iowa</option>
                  <option value="KS">Kansas</option>
                  <option value="KY">Kentucky</option>
                  <option value="LA">Louisiana</option>
                  <option value="ME">Maine</option>
                  <option value="MD">Maryland</option>
                  <option value="MA">Massachusetts</option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">New Hampshire</option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">North Carolina</option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">South Carolina</option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX" selected="selected">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">West Virginia</option>
                  <option value="WI">Wisconsin</option>
                  <option value="WY">Wyoming</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="zip">Zip:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="zip" placeholder="Zip Code" required />
              </div>
            </div>

            <div class="form-row">
              <div class="col">
                <label for="email">Email Address:</label>
              </div>
              <div class="col">
                <input class="form-control" type="text" name="email" placeholder="email@sample.com" required />
                <p id="text-hint">
                  We don't send spam or sell your contact information to anyone.
                </p>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>