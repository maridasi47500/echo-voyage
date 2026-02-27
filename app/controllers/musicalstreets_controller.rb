class MusicalstreetsController < ApplicationController
  before_action :set_musicalstreet, only: %i[ show edit update destroy ]

  # GET /musicalstreets or /musicalstreets.json
  def index
    @musicalstreets = Musicalstreet.all
  end

  # GET /musicalstreets/1 or /musicalstreets/1.json
  def show
  end

  # GET /musicalstreets/new
  def new
    @musicalstreet = Musicalstreet.new
  end

  # GET /musicalstreets/1/edit
  def edit
  end

  # POST /musicalstreets or /musicalstreets.json
  def create
    @musicalstreet = Musicalstreet.new(musicalstreet_params)

    respond_to do |format|
      if @musicalstreet.save
        format.html { redirect_to @musicalstreet, notice: "Musicalstreet was successfully created." }
        format.json { render :show, status: :created, location: @musicalstreet }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @musicalstreet.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /musicalstreets/1 or /musicalstreets/1.json
  def update
    respond_to do |format|
      if @musicalstreet.update(musicalstreet_params)
        format.html { redirect_to @musicalstreet, notice: "Musicalstreet was successfully updated.", status: :see_other }
        format.json { render :show, status: :ok, location: @musicalstreet }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @musicalstreet.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /musicalstreets/1 or /musicalstreets/1.json
  def destroy
    @musicalstreet.destroy!

    respond_to do |format|
      format.html { redirect_to musicalstreets_path, notice: "Musicalstreet was successfully destroyed.", status: :see_other }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_musicalstreet
      @musicalstreet = Musicalstreet.find(params.expect(:id))
    end

    # Only allow a list of trusted parameters through.
    def musicalstreet_params
      params.expect(musicalstreet: [ :lieu, :lat, :lon ])
    end
end
