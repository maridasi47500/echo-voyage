require "test_helper"

class MusicalstreetsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @musicalstreet = musicalstreets(:one)
  end

  test "should get index" do
    get musicalstreets_url
    assert_response :success
  end

  test "should get new" do
    get new_musicalstreet_url
    assert_response :success
  end

  test "should create musicalstreet" do
    assert_difference("Musicalstreet.count") do
      post musicalstreets_url, params: { musicalstreet: { lat: @musicalstreet.lat, lieu: @musicalstreet.lieu, lon: @musicalstreet.lon } }
    end

    assert_redirected_to musicalstreet_url(Musicalstreet.last)
  end

  test "should show musicalstreet" do
    get musicalstreet_url(@musicalstreet)
    assert_response :success
  end

  test "should get edit" do
    get edit_musicalstreet_url(@musicalstreet)
    assert_response :success
  end

  test "should update musicalstreet" do
    patch musicalstreet_url(@musicalstreet), params: { musicalstreet: { lat: @musicalstreet.lat, lieu: @musicalstreet.lieu, lon: @musicalstreet.lon } }
    assert_redirected_to musicalstreet_url(@musicalstreet)
  end

  test "should destroy musicalstreet" do
    assert_difference("Musicalstreet.count", -1) do
      delete musicalstreet_url(@musicalstreet)
    end

    assert_redirected_to musicalstreets_url
  end
end
