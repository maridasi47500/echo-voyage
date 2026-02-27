require "application_system_test_case"

class MusicalstreetsTest < ApplicationSystemTestCase
  setup do
    @musicalstreet = musicalstreets(:one)
  end

  test "visiting the index" do
    visit musicalstreets_url
    assert_selector "h1", text: "Musicalstreets"
  end

  test "should create musicalstreet" do
    visit musicalstreets_url
    click_on "New musicalstreet"

    fill_in "Lat", with: @musicalstreet.lat
    fill_in "Lieu", with: @musicalstreet.lieu
    fill_in "Lon", with: @musicalstreet.lon
    click_on "Create Musicalstreet"

    assert_text "Musicalstreet was successfully created"
    click_on "Back"
  end

  test "should update Musicalstreet" do
    visit musicalstreet_url(@musicalstreet)
    click_on "Edit this musicalstreet", match: :first

    fill_in "Lat", with: @musicalstreet.lat
    fill_in "Lieu", with: @musicalstreet.lieu
    fill_in "Lon", with: @musicalstreet.lon
    click_on "Update Musicalstreet"

    assert_text "Musicalstreet was successfully updated"
    click_on "Back"
  end

  test "should destroy Musicalstreet" do
    visit musicalstreet_url(@musicalstreet)
    click_on "Destroy this musicalstreet", match: :first

    assert_text "Musicalstreet was successfully destroyed"
  end
end
